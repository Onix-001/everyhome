import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from .models import Message, Conversation

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        # Récupérer la dernière conversation de cet utilisateur
        if self.user.is_staff:
            self.conversation = await sync_to_async(lambda: Conversation.objects.filter(admin=self.user).last())()
        else:
            self.conversation = await sync_to_async(lambda: Conversation.objects.filter(client=self.user).last())()

        # Si aucune conversation n'existe, créer une nouvelle
        if not self.conversation:
            if self.user.is_staff:
                self.conversation = await sync_to_async(Conversation.objects.create)(admin=self.user)
            else:
                self.conversation = await sync_to_async(Conversation.objects.create)(client=self.user)

        # Nom du groupe basé sur l'id de la conversation
        self.room_group_name = f"chat_{self.conversation.id}"

        # Rejoindre le groupe
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"🔥 WEBSOCKET CONNECTÉ pour {self.user.username} (conversation {self.conversation.id}) 🔥")

    async def disconnect(self, close_code):
        # Quitter le groupe
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print(f"❌ WEBSOCKET DÉCONNECTÉ pour {self.user.username} ❌")

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_text = data.get("message")

        if message_text:
            # Sauvegarder le message en base
            message = await sync_to_async(Message.objects.create)(
                conversation=self.conversation,
                sender=self.user,
                content=message_text
            )

            # Envoyer le message à tous les membres du groupe
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message.content,
                    "sender": self.user.username,
                    "is_admin": self.user.is_staff,
                    "timestamp": message.timestamp.strftime("%H:%M %d/%m/%Y"),
                    "avatar": getattr(self.user, "avatar_url", None)  # si tu as un champ avatar
                }
            )

    # Réception d'un message du groupe
    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
