from django import forms
from .models import Users

names = Users.objects.all()

class UploadFileForm(forms.Form):
    name = forms.ModelChoiceField(queryset = names)
    uploadedFile = forms.FileField()

class TestResults(forms.Form):
    passwd = forms.PasswordInput()