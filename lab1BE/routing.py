from django.urls import re_path

from .consumers import OnlineStatusConsumer, TodoConsumer

websocket_urlpatterns = [
    re_path(r'ws/online/$', OnlineStatusConsumer.as_asgi()),
    re_path(r'ws/todo/$', TodoConsumer.as_asgi()),
]