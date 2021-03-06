from django.conf.urls import patterns, include, url
from cc import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cc.views.home', name='home'),
    # url(r'^cc/', include('cc.foo.urls')),
    (r'^',include('apps.auth.urls')),
    (r'^',include('apps.api.urls')),
    (r'^',include('apps.dashboard.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
