from apps.dashboard.forms import *
import datetime
from apps.api.views import *
from apps.api.models import *
import json
from itertools import chain
from apps.api.helpers import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext

@login_required
def dashboard(request):
        
        queries = WebQuery.objects.using('launchg').order_by('date_time')   # will fetch the objects from the table
        chat_data = chat_query(queries)
        cc_user = request.user.id
        
        form = CcReply()

        if request.method == 'POST':
            rr_reply(request)
        
        return render_to_response('dashboard/dashboard.html', {'form': form, 'chat_data' : chat_data,} , context_instance = RequestContext(request))