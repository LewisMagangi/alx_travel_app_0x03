from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer

from .tasks import send_booking_confirmation_email

class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

	def perform_create(self, serializer):
		booking = serializer.save()
		# Prepare email details
		to_email = booking.user.email if hasattr(booking, 'user') and booking.user else None
		subject = 'Booking Confirmation'
		message = f'Thank you for your booking, {getattr(booking.user, "username", "Guest")}! Your booking ID is {booking.id}.'
		if to_email:
			send_booking_confirmation_email.delay(to_email, subject, message)
