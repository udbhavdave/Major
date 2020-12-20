from django.forms import ModelForm
from django import forms
from .models import *


# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ['image']

class UploadForm(forms.Form):
    upload=forms.FileField(required=False)


class SearchForm(forms.Form):
    search=forms.CharField(max_length=200, required=False)
