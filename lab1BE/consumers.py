import json
from channels.generic.websocket import AsyncWebsocketConsumer


class OnlineStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        user_id = data['profileId']
        is_online = data['is_active']

        await self.channel_layer.group_send(
            'online_users_group',
            {
                'type': 'user_status',
                'user_id': user_id,
                'is_online': is_online
            }
        )

    async def user_status(self, event):
        user_id = event['profileId']
        is_online = event['is_active']

        # Відправка повідомлення про онлайн статус користувача на клієнт
        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'is_online': is_online
        }))


class TodoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        todo = data.copy()

        await self.channel_layer.group_send(
            'todos_group',
            {
                'type': 'todo_message',
                'todo': todo
            }
        )

    async def todo_message(self, event):
        todo_id = event['identifier']

        await self.send(text_data=json.dumps({
            'todo_message': todo_id
        }))
