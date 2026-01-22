from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Conversation(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="client_conversations"
    )
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="admin_conversations"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('client', 'admin')
        ordering = ['-created_at']

    def __str__(self):
        return f"Conversation {self.client} ↔ {self.admin}"


class Message(models.Model):
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",
        null=True,       # <- autorise les messages sans conversation existante
        blank=True       # <- autorise vide dans les formulaires
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender} : {self.content[:30]}"
