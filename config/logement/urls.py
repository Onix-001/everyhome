from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path 
app_name = 'logement'

urlpatterns = [
    path('logement/', views.logement, name='logement'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )