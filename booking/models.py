from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#time slots for booking availability.
time_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)

# status options for bookings.
status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)

# Model to manage restaurant tables.
class Table(models.Model):
    table_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=50, default='New Table', unique=True)
    max_seats = models.PositiveIntegerField(default=2)

    class Meta:
        ordering = ['-max_seats']

    def __str__(self):
        return self.table_name


# Model to manage the booking system.
class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(max_length=25, choices=time_slots, default='17:00')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="bookings", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings", null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, default="")
    status = models.CharField(max_length=25, choices=status_options, default='Awaiting confirmation')
    guest_count = models.IntegerField(choices=[(i, f"{i} Guests") for i in range(1, 7)], default=2)

    class Meta:
        ordering = ['-requested_date', '-requested_time']
        unique_together = ('table', 'requested_date', 'requested_time')

    def __str__(self):
        return f"{self.status} - {self.requested_time} on {self.requested_date}"