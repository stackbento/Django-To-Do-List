from django import forms
from . models import List


class ListForm(forms.ModelForm):
    class Meta:
        model = List #the main model from models.py 
        fields = ['item', 'is_completed'] # accessing the required fields from the model