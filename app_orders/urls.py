from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.buy_view),
    path('stripe-key', views.get_stripe_key),
    path('payment-success/', views.payment_success, name='payment_success'),
    path('payment-cancel/', views.payment_cancel, name='payment_cancel'),
]
