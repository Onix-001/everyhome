from django.contrib import admin
from .models import Categorie, Logement, ImageLogement


# ---------- INLINE IMAGES ----------
class ImageLogementInline(admin.TabularInline):
    model = ImageLogement
    extra = 1
    fields = ('image', 'description')


# ---------- CATEGORIE ----------
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom_categorie')
    search_fields = ('nom_categorie',)
    ordering = ('nom_categorie',)


# ---------- LOGEMENT ----------
@admin.register(Logement)
class LogementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titre',
        'ville',
        'prix_par_nuit',
        'capacite',
        'statut_logement',
        'categorie',
        'proprietaire',
        'date_creation',
    )

    list_filter = (
        'ville',
        'statut_logement',
        'categorie',
    )

    search_fields = (
        'titre',
        'ville',
        'adresse',
        'proprietaire__username',
    )

    readonly_fields = ('date_creation',)

    inlines = [ImageLogementInline]

    fieldsets = (
        ('Informations générales', {
            'fields': (
                'titre',
                'description',
                'categorie',
                'statut_logement',
            )
        }),
        ('Localisation', {
            'fields': (
                'adresse',
                'ville',
            )
        }),
        ('Détails', {
            'fields': (
                'prix_par_nuit',
                'capacite',
                'proprietaire',
            )
        }),
        ('Système', {
            'fields': (
                'date_creation',
            )
        }),
    )


# ---------- IMAGE LOGEMENT ----------
@admin.register(ImageLogement)
class ImageLogementAdmin(admin.ModelAdmin):
    list_display = ('id', 'logement', 'image')
    search_fields = ('logement__titre',)
