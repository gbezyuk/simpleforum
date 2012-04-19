from django.contrib import admin
from .models import Room

class RoomAdmin(admin.ModelAdmin):
    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]

    save_on_top = True

admin.site.register(Room, RoomAdmin)