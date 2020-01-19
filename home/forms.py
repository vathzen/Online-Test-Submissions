from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20)
    uploadedFile = forms.FileField(label='Answer Script:')