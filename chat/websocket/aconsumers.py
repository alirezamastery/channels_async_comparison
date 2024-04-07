import json

from channels.db import database_sync_to_async
from django.core.cache import cache
from django.conf import settings
from channels.generic.websocket import AsyncWebsocketConsumer


class AsyncConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
