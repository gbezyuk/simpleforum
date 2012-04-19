from django.views.generic.simple import direct_to_template
from .models import Room

def index(request, template_name='simpleforum/index.haml'):
    """Forum index view"""
    rooms = Room.objects.filter(parent=None)
    return direct_to_template(request, template_name, locals())
