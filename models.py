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

class ApiRepresentative(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    user = models.ForeignKey('AuthUser')
    class Meta:
        db_table = 'api_representative'

class Area(models.Model):
    area_id = models.BigIntegerField(unique=True)
    area_name = models.CharField(max_length=50)
    class Meta:
        db_table = 'area'

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80, unique=True)
    class Meta:
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    permission = models.ForeignKey('AuthPermission')
    class Meta:
        db_table = 'auth_group_permissions'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = 'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    group = models.ForeignKey(AuthGroup)
    class Meta:
        db_table = 'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    permission = models.ForeignKey(AuthPermission)
    class Meta:
        db_table = 'auth_user_user_permissions'

class Business2(models.Model):
    business_id = models.BigIntegerField(unique=True)
    b_name = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=50)
    b_add = models.CharField(max_length=1000)
    area_id = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    class Meta:
        db_table = 'business2'

class BusinessReply(models.Model):
    msg_id = models.BigIntegerField(unique=True)
    conversation_id = models.BigIntegerField()
    business_id = models.BigIntegerField()
    query_id = models.BigIntegerField()
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'business_reply'

class Businessnew(models.Model):
    business_id = models.BigIntegerField(unique=True)
    b_name = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=50)
    b_add = models.CharField(max_length=1000)
    area_id = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    url = models.CharField(max_length=500)
    class Meta:
        db_table = 'businessnew'

class BusinessnewBackup(models.Model):
    business_id = models.BigIntegerField(unique=True)
    b_name = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=50)
    b_add = models.CharField(max_length=1000)
    area_id = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup'

class BusinessnewBackup1(models.Model):
    business_id = models.BigIntegerField(unique=True)
    b_name = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=50)
    b_add = models.CharField(max_length=1000)
    area_id = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup1'

class BusinessnewBackup2(models.Model):
    business_id = models.BigIntegerField(unique=True)
    b_name = models.CharField(max_length=50)
    b_phone = models.CharField(max_length=50)
    b_add = models.CharField(max_length=1000)
    area_id = models.CharField(max_length=50)
    categories = models.CharField(max_length=1000)
    rating = models.IntegerField()
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    home_delivery = models.IntegerField(db_column='Home Delivery') # Field name made lowercase. Field renamed to remove unsuitable characters.
    credit_card_facility = models.IntegerField(db_column='Credit Card facility') # Field name made lowercase. Field renamed to remove unsuitable characters.
    menu_available = models.IntegerField(db_column='Menu Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    bar_available = models.IntegerField(db_column='Bar Available') # Field name made lowercase. Field renamed to remove unsuitable characters.
    dine_in = models.IntegerField(db_column='Dine In') # Field name made lowercase. Field renamed to remove unsuitable characters.
    pure_vegetarian = models.IntegerField(db_column='Pure Vegetarian') # Field name made lowercase. Field renamed to remove unsuitable characters.
    cost = models.CharField(max_length=255, db_column='Cost') # Field name made lowercase.
    timings = models.CharField(max_length=255, db_column='Timings') # Field name made lowercase.
    check = models.IntegerField()
    class Meta:
        db_table = 'businessnew_backup2'

class Businessowners(models.Model):
    b_phone = models.CharField(max_length=50)
    b_id = models.IntegerField()
    userid = models.IntegerField(primary_key=True, db_column='UserID') # Field name made lowercase.
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=32, db_column='Password') # Field name made lowercase.
    b_name = models.CharField(max_length=100)
    b_address = models.CharField(max_length=255)
    class Meta:
        db_table = 'businessowners'

class Categories(models.Model):
    id = models.IntegerField(primary_key=True)
    cat = models.CharField(max_length=255)
    syn = models.CharField(max_length=100)
    class Meta:
        db_table = 'categories'

class CcChatData(models.Model):
    conversation_id = models.CharField(max_length=64, unique=True)
    reply_from = models.IntegerField()
    b_id = models.IntegerField()
    q_id = models.IntegerField()
    reply_id = models.IntegerField()
    class Meta:
        db_table = 'cc_chat_data'

class CcUser(models.Model):
    name = models.CharField(max_length=64)
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    class Meta:
        db_table = 'cc_user'

class CiSessions(models.Model):
    session_id = models.CharField(max_length=40, unique=True)
    ip_address = models.CharField(max_length=45)
    user_agent = models.CharField(max_length=120)
    last_activity = models.IntegerField()
    user_data = models.TextField()
    class Meta:
        db_table = 'ci_sessions'

class DataCcUser(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    class Meta:
        db_table = 'data_cc_user'

class DataCcuser(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    phone = models.IntegerField()
    gender = models.CharField(max_length=1)
    user = models.ForeignKey(AuthUser)
    class Meta:
        db_table = 'data_ccuser'

class DataCcusers(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    text = models.TextField()
    class Meta:
        db_table = 'data_ccusers'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user = models.ForeignKey(AuthUser)
    content_type = models.ForeignKey('DjangoContentType', null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = 'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = 'django_content_type'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = 'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'django_site'

class Query(models.Model):
    query_id = models.BigIntegerField(unique=True)
    conversation_id = models.BigIntegerField()
    gcm_id = models.CharField(max_length=1000)
    user_id = models.BigIntegerField()
    what = models.CharField(max_length=20)
    where = models.CharField(max_length=500)
    message = models.CharField(max_length=200)
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'query'

class QueryBusiness(models.Model):
    id = models.IntegerField(primary_key=True)
    business_id = models.CharField(max_length=10)
    query_id = models.BigIntegerField()
    date_time = models.DateTimeField()
    class Meta:
        db_table = 'query_business'

class TzMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    usr = models.CharField(max_length=32, unique=True)
    pass_field = models.CharField(max_length=32, db_column='pass') # Field renamed because it was a Python reserved word.
    email = models.CharField(max_length=255)
    regip = models.CharField(max_length=15, db_column='regIP') # Field name made lowercase.
    dt = models.DateTimeField()
    class Meta:
        db_table = 'tz_members'

class Users(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=20)
    fb_token = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    fb_likes = models.TextField()
    twitter = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    gcm_id = models.CharField(max_length=1000)
    date_time = models.DateTimeField()
    last_login = models.DateTimeField()
    last_push = models.DateTimeField()
    class Meta:
        db_table = 'users'

class WebQuery(models.Model):
    id = models.IntegerField(primary_key=True)
    query_id = models.BigIntegerField(unique=True)
    conversation_id = models.CharField(max_length=50)
    u_id = models.CharField(max_length=50)
    u_query = models.CharField(max_length=500)
    sent_to = models.CharField(max_length=500)
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
    conversation_id = models.CharField(max_length=50)
    b_id = models.CharField(max_length=20)
    u_query = models.CharField(max_length=500)
    user_id = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    diff = models.IntegerField()
    class Meta:
        db_table = 'web_reply'

class WebUsers(models.Model):
    user_id = models.BigIntegerField(unique=True)
    username = models.CharField(max_length=20)
    fb_token = models.CharField(max_length=1000)
    email = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    fb_likes = models.TextField()
    twitter = models.CharField(max_length=50)
    gmail = models.CharField(max_length=50)
    gcm_id = models.CharField(max_length=1000)
    date_time = models.DateTimeField()
    last_login = models.DateTimeField()
    class Meta:
        db_table = 'web_users'

