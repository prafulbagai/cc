from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect,render
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth.views import logout,login

@login_required
def home(request):
	ctx = {}
	return render_to_response('auth/home.html',ctx, context_instance = RequestContext(request))

def register(request):
	form = RegisterForm(request.POST or None)
	
	if(form.is_valid()):
		user = form.save()
		
def login_page(request):
	
	if request.user.is_authenticated():
		return redirect('/dashboard')
	else:
		return login(request)
