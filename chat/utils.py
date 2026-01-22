from django.contrib.auth import get_user_model
from .models import Conversation

User = get_user_model()

def get_or_create_conversation(user):
    if user.is_staff:
        # Admin : rejoindre la conversation du client le plus récent
        return Conversation.objects.last()
    else:
        # Client : conversation avec un admin
        admin = User.objects.filter(is_staff=True).first()
        conversation, created = Conversation.objects.get_or_create(
            client=user,
            admin=admin
        )
        return conversation
