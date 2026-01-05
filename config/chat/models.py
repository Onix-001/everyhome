from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    client = models.ForeignKey(User, related_name="client_room", on_delete=models.CASCADE)
    admin = models.ForeignKey(User, related_name="admin_room", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat {self.client.username} - {self.admin.username}"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]
