from apps.api.helpers import *
from itertools import chain
from django.http import HttpResponse

def get_unread_queries(request):
	results = db_query()
	
	return HttpResponse(results)

