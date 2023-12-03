from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>', views.item_view, name='item_detail'),
    path('', views.index),
]
