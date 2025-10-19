
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Listing(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	location = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available_from = models.DateField()
	available_to = models.DateField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title



class Booking(models.Model):
	listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
	user = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
	start_date = models.DateField()
	end_date = models.DateField()
	status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='pending')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Booking for {self.listing.title} by {self.user}"



class Payment(models.Model):
	booking = models.ForeignKey(Booking, related_name='payments', on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=10, decimal_places=2)
	transaction_id = models.CharField(max_length=100, blank=True, null=True)
	status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Payment for Booking {self.booking.id} - {self.status}"
