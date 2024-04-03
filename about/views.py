from django.shortcuts import render
from .models import AboutUs

# Create your views here.
def about_us(request):
    """
    Renders the About Us page
    """
    about = AboutUs.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/aboutus.html",
        {"about": about},
    )
