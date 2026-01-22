from django.db import models
from django.conf import settings

class Categorie(models.Model):
    nom_categorie = models.CharField(max_length=100)
    desscription = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.nom_categorie
class Logement(models.Model):
    statut_choices = [
        ('disponible', 'Disponible'),
        ('indisponible', 'Indisponible'),
        ('occupe', 'Occupé'),
    ]
    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    adresse = models.CharField(max_length=300)
    ville = models.CharField(max_length=100)
    prix_par_nuit =   models.FloatField()
    capacite = models.PositiveIntegerField()
    statut_logement = models.CharField(max_length=20, choices=statut_choices, default='disponible')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='logements')
    proprietaire = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logements')  
    date_creation = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titre

class ImageLogement(models.Model):
    logement = models.ForeignKey(
        Logement,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='logements/')
    description = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"Image - {self.logement.titre}"

# Create your models here.
