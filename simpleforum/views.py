from django.utils.translation import ugettext_lazy as _
from django.views.generic.simple import direct_to_template, redirect_to
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Room
from .forms import RoomForm

def index(request, template_name='simpleforum/index.haml'):
    """
    Forum index view
    """
    rooms = Room.objects.filter(parent=None)
    return direct_to_template(request, template_name, locals())

def add_room(request, parent_room_id=None, template_name='simpleforum/add_room.haml'):
    """
    Forum add room form view
    """
    room=None
    if parent_room_id:
      room = get_object_or_404(Room, pk=parent_room_id)
    form = RoomForm(parent_room=room,data = request.POST or None, initial=Room.get_initials())
    if form.is_valid():
        form.save()
        messages.success(request, _('room was successfully added'))
        return redirect_to(request, reverse('simpleforum_index'), permanent=False)
    return direct_to_template(request, template_name, locals())

def room(request, room_id, template_name='simpleforum/room.haml'):
    room = get_object_or_404(Room, pk=room_id)
    rooms = room.children.all()
    return direct_to_template(request, template_name, locals())