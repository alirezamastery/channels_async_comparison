import json

from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
from django.core.cache import cache
from django.conf import settings
from channels.generic.websocket import WebsocketConsumer


class Consumer(WebsocketConsumer):

    def connect(self):
        print('connect')

        for i in range(10000):
            async_to_sync(self.channel_layer.group_add)(f'room_{i}', self.channel_name)

        self.accept()
