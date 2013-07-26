from django import forms
   
class CcReply(forms.Form):
    reply = forms.CharField()
    