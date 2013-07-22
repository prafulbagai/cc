from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'dashboard/', 'apps.dashboard.views.dashboard', name = 'dashboard'),
		)