from django.db import models
from django.contrib.auth.models import User

# Ajouter téléphone au User standard
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        # Affiche le nom complet pour plus de clarté
        return f"{self.user.first_name} {self.user.last_name} ({self.user.username})"
