from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path 
app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    path('homereservation/', views.homereservation, name='homereservation'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/', views.detail, name='detail'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )