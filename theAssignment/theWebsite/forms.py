from django import forms
from .models import *

# body of the form
class theForm(forms.ModelForm):
    ## this is from back when i was using the check api function
    ##words = forms.CharField(label="Text", max_length=100)
    class Meta:
        model = pictureStore
        fields = ['picture']