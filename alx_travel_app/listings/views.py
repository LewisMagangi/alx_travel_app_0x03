from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer
import os
import requests


class ListingViewSet(viewsets.ModelViewSet):
	queryset = Listing.objects.all()
	serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer

class PaymentViewSet(viewsets.ModelViewSet):
	queryset = Payment.objects.all()
	serializer_class = PaymentSerializer

# Chapa Payment Initiation API
class InitiatePaymentAPIView(APIView):
	def post(self, request):
		booking_id = request.data.get('booking_id')
		amount = request.data.get('amount')
		booking = Booking.objects.get(id=booking_id)
		chapa_secret = os.getenv('CHAPA_SECRET_KEY')
		if not chapa_secret:
			return Response({'error': 'Chapa secret key not configured.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

		# Prepare Chapa API payload
		payload = {
			"amount": str(amount),
			"currency": "ETB",
			"email": booking.user.email,
			"first_name": booking.user.first_name,
			"last_name": booking.user.last_name,
			"tx_ref": f"booking_{booking.id}",
			"callback_url": request.build_absolute_uri('/api/payment/verify/')
		}
		headers = {
			"Authorization": f"Bearer {chapa_secret}"
		}
		response = requests.post("https://api.chapa.co/v1/transaction/initialize", json=payload, headers=headers)
		data = response.json()
		if response.status_code == 200 and data.get('status') == 'success':
			transaction_id = data['data']['tx_ref']
			payment = Payment.objects.create(
				booking=booking,
				amount=amount,
				transaction_id=transaction_id,
				status='pending'
			)
			return Response({
				'checkout_url': data['data']['checkout_url'],
				'payment_id': payment.id
			}, status=status.HTTP_201_CREATED)
		else:
			return Response({'error': data.get('message', 'Payment initiation failed.')}, status=status.HTTP_400_BAD_REQUEST)
