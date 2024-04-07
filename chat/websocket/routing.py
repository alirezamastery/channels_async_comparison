from django.urls import path

from .consumers import Consumer
from .aconsumers import AsyncConsumer


websocket_urlpatterns = [
    path('ws/', Consumer.as_asgi()),
    path('ws2/', AsyncConsumer.as_asgi()),
]
