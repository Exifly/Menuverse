
from django import forms
from .models import FeedBack

class FeedBackeForm(forms.Form):

 class Meta:
   model = FeedBack
   fields = ['nome', 'messaggio']
