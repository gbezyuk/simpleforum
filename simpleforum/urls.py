from django.conf.urls import patterns, url
from .views import index, room, add_room

urlpatterns = patterns('',
    url(r'^$', index, name='simpleforum_index'),
    url(r'^(?P<room_id>\d+)/$', room, name='simpleforum_room'),
    url(r'^add_room/$', add_room, name='simpleforum_add_room'),
    url(r'^(?P<parent_room_id>\d+)/add_room/$', add_room, name='simpleforum_insert_room'),
)