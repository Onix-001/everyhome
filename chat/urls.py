from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import chat_view
app_name = "chat"

urlpatterns = [
    path("chat/", views.chat_view, name="chat"),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
