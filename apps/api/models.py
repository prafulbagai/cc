# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Area(models.Model):
    area_id = models.BigIntegerField(primary_key=True)
    area_name = models.CharField(max_length=50L)
    class Meta:
        db_table = 'area'

class Business2(models.Model):
    business_id = models.BigIntegerField(primary_key=True)
    b_name = models.CharField(max_length=50L)
    b_phone = models.CharField(max_length=50L)
    b_add = models.CharField(max_length=1000L)
    area_id = models.CharField(max_length=50L)
    categories = models.CharField(max_length=1000L)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255L)
    longitude = models.CharField(max_length=255L)
    class Meta:
        db_table = 'business2'

class BusinessReply(models.Model):
    msg_id = models.BigIntegerField(primary_key=True)
    conversation_id = models.BigIntegerField()
    business_id = models.BigIntegerField()
    query_id = models.BigIntegerField()
    username = models.CharField(max_length=50L)
    message = models.CharField(max_length=500L)
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'business_reply'

class Businessnew(models.Model):
    business_id = models.BigIntegerField(primary_key=True)
    b_name = models.CharField(max_length=50L)
    b_phone = models.CharField(max_length=50L)
    b_add = models.CharField(max_length=1000L)
    area_id = models.CharField(max_length=50L)
    categories = models.CharField(max_length=1000L)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255L)
    longitude = models.CharField(max_length=255L)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255L, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255L, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    url = models.CharField(max_length=500L)
    class Meta:
        db_table = 'businessnew'

class BusinessnewBackup(models.Model):
    business_id = models.BigIntegerField(primary_key=True)
    b_name = models.CharField(max_length=50L)
    b_phone = models.CharField(max_length=50L)
    b_add = models.CharField(max_length=1000L)
    area_id = models.CharField(max_length=50L)
    categories = models.CharField(max_length=1000L)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255L)
    longitude = models.CharField(max_length=255L)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255L, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255L, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup'

class BusinessnewBackup1(models.Model):
    business_id = models.BigIntegerField(primary_key=True)
    b_name = models.CharField(max_length=50L)
    b_phone = models.CharField(max_length=50L)
    b_add = models.CharField(max_length=1000L)
    area_id = models.CharField(max_length=50L)
    categories = models.CharField(max_length=1000L)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255L)
    longitude = models.CharField(max_length=255L)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255L, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255L, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup1'

class BusinessnewBackup2(models.Model):
    business_id = models.BigIntegerField(primary_key=True)
    b_name = models.CharField(max_length=50L)
    b_phone = models.CharField(max_length=50L)
    b_add = models.CharField(max_length=1000L)
    area_id = models.CharField(max_length=50L)
    categories = models.CharField(max_length=1000L)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255L)
    longitude = models.CharField(max_length=255L)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255L, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255L, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup2'

class Businessowners(models.Model):
    b_phone = models.CharField(max_length=50L)
    b_id = models.IntegerField()
    userid = models.IntegerField(primary_key=True, db_column='UserID') # Field name made lowercase.
    firstname = models.CharField(max_length=100L)
    lastname = models.CharField(max_length=100L)
    email = models.CharField(max_length=150L)
    password = models.CharField(max_length=32L, db_column='Password') # Field name made lowercase.
    b_name = models.CharField(max_length=100L)
    b_address = models.CharField(max_length=255L)
    class Meta:
        db_table = 'businessowners'

class Categories(models.Model):
    cat = models.CharField(max_length=255L)
    syn = models.CharField(max_length=100L)
    class Meta:
        db_table = 'categories'

class CiSessions(models.Model):
    session_id = models.CharField(max_length=40L, primary_key=True)
    ip_address = models.CharField(max_length=45L)
    user_agent = models.CharField(max_length=120L)
    last_activity = models.IntegerField()
    user_data = models.TextField()
    class Meta:
        db_table = 'ci_sessions'

class Query(models.Model):
    query_id = models.BigIntegerField(primary_key=True)
    conversation_id = models.BigIntegerField()
    gcm_id = models.CharField(max_length=1000L)
    user_id = models.BigIntegerField()
    what = models.CharField(max_length=20L)
    where = models.CharField(max_length=500L)
    message = models.CharField(max_length=200L)
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'query'

class QueryBusiness(models.Model):
    business_id = models.CharField(max_length=10L)
    query_id = models.BigIntegerField()
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'query_business'

class TzMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.CharField(max_length=32L, unique=True)
    pass_field = models.CharField(max_length=32L, db_column='pass') # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=255L)
    regip = models.CharField(max_length=15L, db_column='regIP') # Field name made lowercase.
    dt = models.DateTimeField()
    class Meta:
        db_table = 'tz_members'

class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20L)
    fb_token = models.CharField(max_length=1000L)
    email = models.CharField(max_length=50L)
    facebook = models.CharField(max_length=50L)
    fb_likes = models.TextField()
    twitter = models.CharField(max_length=50L)
    gmail = models.CharField(max_length=50L)
    gcm_id = models.CharField(max_length=1000L)
    date_time = models.DateTimeField()
    last_login = models.DateTimeField()
    last_push = models.DateTimeField()
    class Meta:
        db_table = 'users'

class WebQuery(models.Model):
    query_id = models.BigIntegerField(primary_key=True)
    conversation_id = models.CharField(max_length=50L)
    u_id = models.CharField(max_length=50L)
    u_query = models.CharField(max_length=500L)
    sent_to = models.CharField(max_length=500L)
    date_time = models.DateTimeField()
    is_reply = models.IntegerField()
    is_responded = models.IntegerField()
    from_gingr = models.IntegerField()
    diff = models.IntegerField()
    class Meta:
        db_table = 'web_query'

class WebReply(models.Model):
    reply_id = models.IntegerField(primary_key=True)
    query_id = models.BigIntegerField()
    conversation_id = models.CharField(max_length=50L)
    b_id = models.CharField(max_length=20L)
    u_query = models.CharField(max_length=500L)
    user_id = models.CharField(max_length=20L)
    date_time = models.DateTimeField()
    diff = models.IntegerField()
    class Meta:
        db_table = 'web_reply'

class WebUsers(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=20L)
    fb_token = models.CharField(max_length=1000L)
    email = models.CharField(max_length=50L)
    facebook = models.CharField(max_length=50L)
    fb_likes = models.TextField()
    twitter = models.CharField(max_length=50L)
    gmail = models.CharField(max_length=50L)
    gcm_id = models.CharField(max_length=1000L)
    date_time = models.DateTimeField()
    last_login = models.DateTimeField()
    class Meta:
        db_table = 'web_users'