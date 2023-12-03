from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/', include('app_items.urls')),
    path('buy/', include('app_orders.urls')),
]
