from django.urls import path
from . import views

urlpatterns = [
    # Add your URL pattern here
    path('', views.payment_request_view, name='payment_request'),
]
