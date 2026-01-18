from django.shortcuts import render, get_object_or_404
from .models import Room, Message
from django.contrib.auth.decorators import login_required

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    messages = Message.objects.filter(room=room).order_by("timestamp")

    if request.method == "POST":
        content = request.POST.get("message")
        Message.objects.create(
            room=room,
            sender=request.user,
            content=content
        )

    return render(request, "chat/room.html", {
        "room": room,
        "messages": messages
    })
