from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel,TreeForeignKey
class Room(MPTTModel):
    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    description = models.TextField(blank=True, null=True, verbose_name=_('description'))
    parent = models.TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=_('parent room'))

    def __unicode__(self):
        return self.title

    @classmethod
    def get_initials(cls):
        return {
            'title': _('new room'),
        }

    @models.permalink
    def get_absolute_url(self):
        return 'simpleforum_room', (), {'room_id': self.pk}