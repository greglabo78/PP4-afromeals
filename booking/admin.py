from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Table, Booking

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_id', 'table_name', 'max_seats')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'name', 'guest_count', 'status', 'table', 'requested_date', 'requested_time', 'created_date')
    list_filter = (
        'user',
        'status',
        ('requested_date', DateRangeFilter),
        'table',
    )
    search_fields = ('name', 'email', 'user__username')
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        queryset.update(status='Booking Confirmed')
        self.message_user(request, "Selected bookings have been confirmed.")

    def get_queryset(self, request):
        """
        Function to improve query performance by reducing the number of database
        queries via select_related and prefetch_related.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('user', 'table')
        return queryset