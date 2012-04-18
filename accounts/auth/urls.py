from django.conf.urls.defaults import patterns, include, url
from accounts.auth.views import *

urlpatterns = patterns('',
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
)