from django import forms
from django.contrib.auth.forms import UserCreationForm
from data.models import CcUser

    
class CcRegister(UserCreationForm):
    name     = forms.CharField()
    phone    = forms.IntegerField() 
    gender   = forms.ChoiceField(choices=CcUser.GENDER)
    
    def save(self, *args, **kwargs):
        user = super(CcRegister,self).save(*args,**kwargs)
        
        CcUser.objects.create(user=user , gender=self.cleaned_data['gender'], name = self.cleaned_data['name'], phone = self.cleaned_data['phone'])
        
        return user
