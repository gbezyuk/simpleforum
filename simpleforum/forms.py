from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude=('parent',)
        
    def __init__(self,*args, **kwargs):
      self.parent_room = kwargs.pop('parent_room', None)
      super(RoomForm, self).__init__(**kwargs)
	  #if parent:
	  
	  
    def  save(self):
      room = super(RoomForm, self).save(commit=False)
      room.parent = self.parent_room
      room.save()
