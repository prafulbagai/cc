from apps.dashboard.forms import *
import datetime
from apps.api.models import *
import json
from itertools import chain
from apps.api.helpers import *
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext

def dashboard(request):
	
	queries = WebQuery.objects.using('launchg').order_by('date_time')   # will fetch the objects from the table
	chat_data = chat_query(queries)
	cc_user = request.user.id
	chatroom_id = request.POST.get('Chatroom','')
	
	form = CcReply()
	
	if request.method == 'POST': 
		
		form = CcReply(request.POST) 
		if form.is_valid():

			conversation_id = chatroom_id.split('_')[0]
			b_id = chatroom_id.split('_')[-1]		
			reply = form.cleaned_data['reply']
			queries = WebQuery.objects.using('launchg').filter(conversation_id = conversation_id)

			r_id = CcChatData.objects.using('launchg').order_by('reply_id')
			for ids in r_id:
				reply_id = ids.reply_id

			for query in queries:
				q_id = query.query_id				
			
			cc_chat_data_obj = CcChatData.objects.using('launchg').create(conversation_id = conversation_id , 
																			reply_from = request.user.id , 
																			b_id = b_id, q_id = q_id, 
																			reply_id = reply_id + 1 )
			web_reply_obj = WebReply.objects.using('launchg').create(query_id = q_id, conversation_id = conversation_id , b_id = b_id, 
				u_query = reply ,diff = 1, user_id = request.user.id, reply_id = reply_id + 1)

			cc_chat_data_obj.save()
			web_reply_obj.save()
			

	else:
		form = CcReply()
	
	return render_to_response('dashboard/dashboard.html', {'form': form, 'chat_data' : chat_data,} , context_instance = RequestContext(request))