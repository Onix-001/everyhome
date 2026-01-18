from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
]

from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path 

app_name = 'account'

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('gesuser', views.gesuser, name='gesuser'),
    path('create', views.create, name='create'),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    
