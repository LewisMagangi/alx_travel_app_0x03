from django.contrib import admin
from .models import Listing, Booking, Payment

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price', 'available_from', 'available_to', 'created_at']
    list_filter = ['location', 'created_at']
    search_fields = ['title', 'description', 'location']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['listing', 'user', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['listing__title', 'user__username']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['booking', 'amount', 'transaction_id', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['transaction_id', 'booking__id']
