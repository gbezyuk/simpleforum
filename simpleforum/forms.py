from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    """
    Add/edit forum room form
    """
    class Meta:
        model = Room
        exclude=('parent',)

    def __init__(self, parent_room=None, **kwargs):
        """
        Constructor stores provided parent room
        """
        self.parent_room = parent_room
        super(RoomForm, self).__init__(**kwargs)

    def save(self, commit=True, **kwargs):
        """
        Save method sets parent room explicitly
        """
        room = super(RoomForm, self).save(commit=False, **kwargs)
        room.parent = self.parent_room
        if commit:
            room.save()
        return room
