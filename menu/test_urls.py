from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

class TestMenuUrls(SimpleTestCase):
    def test_menu_url_is_resolved(self):
        # Use the 'reverse' function to get the URL from the 'name'
        url = reverse('menu')
        # The 'resolve' function is used to determine which view function the URL maps to
        self.assertEquals(resolve(url).func, views.menu_view)
