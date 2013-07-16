from apps.api.models import *
import json
from itertools import chain

def db_query():
	
	replies = []
	queries = WebQuery.objects.using('launchg').filter(is_responded = 0).order_by('date_time')   # will fetch the objects from the table
	for query in queries:
		c_id = query.conversation_id
		b_ids = json.loads(query.sent_to)
		b_ids = b_ids["business_ids"]

		for index in range(len(b_ids)):
			b_ids[index] = int(b_ids[index])

		for b_id in b_ids:
			representative_reply = WebReply.objects.using('launchg').filter(conversation_id = c_id , b_id = b_id).order_by('date_time')
			user_reply = WebQuery.objects.using('launchg').filter(conversation_id = c_id).order_by('date_time')
			replies.append(chain(representative_reply , user_reply))
			business_data = Businessowners.objects.using('launchg').filter(b_id = b_id)
			

	return [replies,business_data]