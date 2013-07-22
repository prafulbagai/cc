from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout


urlpatterns = patterns('',
	url(r'cc/', 'apps.auth.views.login_page', name = 'cc_login'),
	url(r'logout/', logout,kwargs = {'template_name' : 'auth/logout.html'}, name = 'cc_logout'),
	url(r'home/','apps.auth.views.home', name = 'cc_home'),
)