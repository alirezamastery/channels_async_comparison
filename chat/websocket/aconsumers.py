import json

from channels.db import database_sync_to_async
from django.core.cache import cache
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer


class AsyncConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        print('connect')

        for i in range(10000):
            await self.channel_layer.group_add(f'room_{i}', self.channel_name)

        await self.accept()
