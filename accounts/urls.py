from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^auth/', include('accounts.auth.urls', namespace='auth')),
    url(r'^registration/', include('accounts.registration.backends.default.urls')),
)