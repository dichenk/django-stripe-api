from django.http import JsonResponse
import stripe
from django.shortcuts import get_object_or_404
from app_items.models import Item
import os
from django.shortcuts import render, reverse


stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


def buy_view(request, id):
    item = get_object_or_404(Item, pk=id)
    quantity = int(request.GET.get('quantity', 1))

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': quantity,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('payment_success')),
        cancel_url=request.build_absolute_uri(reverse('payment_cancel')),
    )
    return JsonResponse({'sessionId': session.id})


def get_stripe_key(request):
    return JsonResponse({'stripePublicKey': os.environ.get('STRIPE_PUBLIC_KEY')})


def payment_success(request):
    return render(request, 'success.html')


def payment_cancel(request):
    return render(request, 'cancel.html')
