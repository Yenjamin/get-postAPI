from django import forms
from .models import *

# body of the form
class theForm(forms.ModelForm):
    ##words = forms.CharField(label="Text", max_length=100)
    class Meta:
        model = pictureStore
        fields = ['picture']