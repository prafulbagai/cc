from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'cc/api/get_unread', 'apps.api.views.get_unread_queries', name = 'get_unread'),
	url(r'cc/api/rr_reply', 'apps.api.views.rr_reply', name = 'rr_reply'),

	)