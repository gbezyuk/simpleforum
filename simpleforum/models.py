from django.utils.translation import ugettext_lazy as _
from django.db import models
from mptt.models import MPTTModel

class Room(MPTTModel):
    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = _('room')
        verbose_name_plural = _('rooms')

    title = models.CharField(max_length=100, verbose_name=_('title'))
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', verbose_name=_('parent room'))

    def __unicode__(self):
        return self.title