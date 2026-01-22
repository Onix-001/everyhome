from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Message
from .utils import get_or_create_conversation
from django.utils import timezone

@login_required
def chat_view(request):
    conversation = get_or_create_conversation(request.user)
    messages = conversation.messages.order_by("timestamp")

    # Calculer les séparateurs de date
    previous_date = None
    for msg in messages:
        local_ts = timezone.localtime(msg.timestamp)
        msg.local_date = local_ts.date()
        if previous_date != msg.local_date:
            msg.show_date = True
            previous_date = msg.local_date
        else:
            msg.show_date = False


    if request.method == "POST":
        content = request.POST.get("message")
        if content:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content
            )
        return redirect("chat:chat")

    return render(request, "chat/chat.html", {
        "conversation": conversation,
        "messages": messages
    })
