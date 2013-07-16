from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'cc/api/get_unread', 'apps.api.views.get_unread_queries', name = 'get_unread'),

	)