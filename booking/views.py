from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator
from datetime import datetime
from .models import Booking
from .forms import BookingForm

# Create your views here.
#function will retrive logged-in user instance
def get_user_instance(request):
    if request.user.is_authenticated:
        return User.objects.filter(email=request.user.email).first()
    return None

class Bookings(View):
    template_name = 'booking/bookings.html'

    def get(self, request):
        user_email = request.user.email if request.user.is_authenticated else None
        booking_form = BookingForm(initial={'email': user_email})
        return render(request, self.template_name, {'booking_form': booking_form})

    def post(self, request):
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user  # Assuming the user must be logged in
            booking.save()
            messages.success(request, "Booking successful, awaiting confirmation")
            return redirect('confirmed')  # Assuming 'confirmed' is the name of a URL pattern
        return render(request, self.template_name, {'booking_form': booking_form})

class Confirmed(View):
    template_name = 'booking/confirmed.html'

    def get(self, request):
        return render(request, self.template_name)

class BookingList(View):
    template_name = 'booking/booking_list.html'
    paginate_by = 4

    def get(self, request):
        today = datetime.now().date()
        bookings = Booking.objects.filter(user=request.user, requested_date__gte=today).order_by('-created_date')
        paginator = Paginator(bookings, self.paginate_by)
        page_number = request.GET.get('page')
        booking_page = paginator.get_page(page_number)
        return render(request, self.template_name, {'booking_page': booking_page})

# # View to edit an existing booking
class EditBooking(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/edit_booking.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self):
        return reverse('booking_list')  # Assuming 'booking_list' is the name of a URL pattern

# # Function-based view to handle booking cancellation
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')
    return render(request, 'booking/cancel_booking.html', {'booking': booking})

