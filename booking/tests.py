from django.test import TestCase
from unittest.mock import patch
from django.contrib.auth.models import User
from .models import Booking, Table
import datetime

# Create your tests here.
class TestBookingModel(TestCase):
    @patch('django.db.models.Model.save', autospec=True)
    def setUp(self, mock_save):
        # Mocking user and table creation to avoid database hits
        self.user = User(username='testuser', id=1)
        self.table = Table(table_id=1, table_name="Table 1", max_seats=4)
        self.booking = Booking(
            booking_id=1,
            requested_date=datetime.date.today(),
            requested_time='18:00',
            table=self.table,
            user=self.user,
            name="John Doe",
            email="john@example.com",
            status='Awaiting confirmation',
            guest_count=3
        )

    def test_string_representation(self):
        expected_string = f"{self.booking.status} - {self.booking.requested_time} on {self.booking.requested_date}"
        self.assertEqual(str(self.booking), expected_string)

    def test_default_status(self):
        # Ensuring default status is set correctly at initialization
        new_booking = Booking()
        self.assertEqual(new_booking.status, 'Awaiting confirmation')

    def test_default_time_slot(self):
        # Ensuring default time slot is set correctly at initialization
        new_booking = Booking()
        self.assertEqual(new_booking.requested_time, '17:00')