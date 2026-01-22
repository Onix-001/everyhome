from django.contrib import admin
from .models import Conversation, Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'admin', 'created_at')
    list_filter = ('created_at',)
    search_fields = (
        'client__username',
        'client__email',
        'admin__username',
        'admin__email',
    )
    ordering = ('-created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'conversation', 'sender', 'short_content', 'timestamp', 'is_read')
    list_filter = ('timestamp', 'is_read')
    search_fields = ('content', 'sender__username', 'sender__email')
    ordering = ('-timestamp',)

    def short_content(self, obj):
        return obj.content[:30]

    short_content.short_description = 'Message'
