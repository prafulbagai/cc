from apps.api.models import *
import json
from itertools import chain
import operator

def chat_query(queries):
	chat_data = {}
	DATE_FORMAT = "%Y-%m-%d" 
	TIME_FORMAT = "%H:%M:%S"

	for query in queries:
		replies = []
		c_id = query.conversation_id
		u_id = query.u_id
		init_query = query.u_query
		b_ids = json.loads(query.sent_to)
		b_ids = b_ids["business_ids"]

		cc_user_id = CcChatData.objects.using('launchg').filter(conversation_id = c_id)
		user_name = Users.objects.using('launchg').filter(user_id = u_id)

		for user in user_name:
			username = user.username

		for ids in cc_user_id:
			cc_id = ids.reply_from

		cc_user = CcUser.objects.using('launchg')#.filter(id = cc_id)

		for user in cc_user:
			cc_username = user.username

		for index in range(len(b_ids)):
			b_ids[index] = int(b_ids[index])

		for b_id in b_ids:

			representative_reply = WebReply.objects.using('launchg').filter(conversation_id = c_id , b_id = b_id).order_by('date_time')
			user_reply = WebQuery.objects.using('launchg').filter(conversation_id = c_id).order_by('date_time')
			#replies.append(chain(representative_reply , user_reply))
			replies.append(representative_reply)
			#replies.sort(key=operator.attrgetter('date_time'))
						
			reply_dict={"chat":[]}
			for reply in replies:
				
				for r in reply:
					if r in user_reply:
						direction = 1
					else : direction = 0

					reply_dict["chat"].append({"direction" : direction , "text" : r.u_query , 
						"date_time" : r.date_time.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT)) })

			business_data = Businessowners.objects.using('launchg').filter(b_id = b_id)
			business_name = None
			business_id = None
			for data in business_data:
				business_name = data.b_name
				business_id = data.b_id

			if business_name is None:
				business_name = "Unregistered"

			if business_id is None:
				business_registered = "False"
			else : business_registered = "True"
			

			chat_data.update({str(c_id) + '_' + str(b_id) : { "from" : query.u_id , 
							 "from_name" : username,
							 "init_query" : init_query,
							 "date_time" : query.date_time.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT)) , 
							 #"from_cc_id" : cc_id,
							 "from_cc_name" : cc_username, "to_business_name" : business_name, 
							 "business_registered" : business_registered,
							 "chat" : reply_dict["chat"] } } )
			
	
	return chat_data

def db_unread_query():
	
	queries = WebQuery.objects.using('launchg').filter(is_responded = 0).order_by('date_time')   # will fetch the objects from the table
	return chat_query(queries)

def db_rr_reply(conversation_id):
	
	chat_data = {}
	replies = []
	reply_dict={"chat":[]}
	DATE_FORMAT = "%Y-%m-%d" 
	TIME_FORMAT = "%H:%M:%S"

	representative_reply = WebReply.objects.using('launchg').filter(conversation_id = conversation_id ).order_by('date_time')
	user_reply = WebQuery.objects.using('launchg').filter(conversation_id = conversation_id).order_by('date_time')
	replies.append(chain(representative_reply , user_reply))
	
	for reply in replies:
		for r in reply:
	
			if isinstance(r.u_query, WebReply):
				direction = 1
			else : 
				direction = 0
			reply_dict["chat"].append({"direction" : direction , "text" : r.u_query , 
						"date_time" : r.date_time.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT)) })
	return reply_dict