from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.
class TestURLs(SimpleTestCase):
    def test_bookings_url_is_resolved(self):
        url = reverse('bookings')
        self.assertEquals(resolve(url).func.view_class, views.Bookings)

    def test_confirmed_url_is_resolved(self):
        url = reverse('confirmed')
        self.assertEquals(resolve(url).func.view_class, views.Confirmed)

    def test_booking_list_url_is_resolved(self):
        url = reverse('booking_list')
        self.assertEquals(resolve(url).func.view_class, views.BookingList)

    def test_edit_booking_url_is_resolved(self):
        # We need to pass an integer ID to generate the URL
        url = reverse('edit_booking', args=[1])
        self.assertEquals(resolve(url).func.view_class, views.EditBooking)

    def test_cancel_booking_url_is_resolved(self):
        # We need to pass an integer ID to generate the URL
        url = reverse('cancel_booking', args=[1])
        self.assertEquals(resolve(url).func, views.cancel_booking)
