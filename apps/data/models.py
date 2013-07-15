from django.db import models
from django.contrib.auth.models import  User


class CcUser(models.Model):
    name 	= models.CharField(max_length = 64)
    phone	= models.IntegerField()
    GENDER  = (
            	('m', 'Male'),
             	('f', 'Female'),
              )
    
    gender 	= models.CharField(max_length=1, choices=GENDER, default='m')
    user 	= models.ForeignKey(User)
    
    def __unicode__(self):
    	return u"%s" % (self.name)
