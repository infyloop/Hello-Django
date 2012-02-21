from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^',include('polls.urls')),
)

 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))

urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))

