from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer
import os
import requests


def home(request):
    """
    Simple home view that displays available API endpoints
    """
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ALX Travel App API</title>
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                background: white;
                border-radius: 20px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                max-width: 800px;
                width: 100%;
                padding: 40px;
                animation: fadeIn 0.5s ease-in;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            h1 {
                color: #667eea;
                margin-bottom: 10px;
                font-size: 2.5em;
            }
            .tagline {
                color: #666;
                margin-bottom: 30px;
                font-size: 1.1em;
            }
            .status {
                display: inline-block;
                background: #10b981;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                margin-bottom: 30px;
            }
            .endpoints {
                margin-top: 30px;
            }
            .endpoint-group {
                margin-bottom: 25px;
            }
            .endpoint-group h3 {
                color: #333;
                margin-bottom: 15px;
                font-size: 1.3em;
            }
            .endpoint {
                background: #f8f9fa;
                padding: 15px;
                margin: 10px 0;
                border-radius: 10px;
                border-left: 4px solid #667eea;
                transition: all 0.3s ease;
            }
            .endpoint:hover {
                background: #e9ecef;
                transform: translateX(5px);
            }
            .endpoint a {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1em;
            }
            .endpoint a:hover {
                text-decoration: underline;
            }
            .endpoint-desc {
                color: #666;
                font-size: 0.9em;
                margin-top: 5px;
            }
            .footer {
                margin-top: 40px;
                padding-top: 20px;
                border-top: 2px solid #e9ecef;
                text-align: center;
                color: #666;
            }
            .version {
                background: #764ba2;
                color: white;
                padding: 3px 10px;
                border-radius: 5px;
                font-size: 0.85em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌍 ALX Travel App</h1>
            <p class="tagline">Your Gateway to Amazing Travel Experiences</p>
            <span class="status">● API Active</span>
            
            <div class="endpoints">
                <div class="endpoint-group">
                    <h3>🔗 Main API Endpoints</h3>
                    <div class="endpoint">
                        <a href="/api/listings/" target="_blank">/api/listings/</a>
                        <div class="endpoint-desc">Browse and manage travel listings</div>
                    </div>
                    <div class="endpoint">
                        <a href="/api/bookings/" target="_blank">/api/bookings/</a>
                        <div class="endpoint-desc">Handle booking operations</div>
                    </div>
                </div>
                
                <div class="endpoint-group">
                    <h3>📚 Documentation</h3>
                    <div class="endpoint">
                        <a href="/swagger/" target="_blank">/swagger/</a>
                        <div class="endpoint-desc">Interactive API documentation (Swagger UI)</div>
                    </div>
                    <div class="endpoint">
                        <a href="/redoc/" target="_blank">/redoc/</a>
                        <div class="endpoint-desc">Beautiful API documentation (ReDoc)</div>
                    </div>
                </div>
                
                <div class="endpoint-group">
                    <h3>⚙️ Admin</h3>
                    <div class="endpoint">
                        <a href="/admin/" target="_blank">/admin/</a>
                        <div class="endpoint-desc">Django administration panel</div>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>Built with Django & Django REST Framework</p>
                <p style="margin-top: 10px;">
                    <span class="version">v1.0</span>
                </p>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


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
