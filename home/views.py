from django.shortcuts import render
from django.http import HttpResponseRedirect

from home.gapi.googleapi import getService
from googleapiclient.http import MediaFileUpload

from .forms import UploadFileForm

import os

# Create your views here.

def index(request):
    service = getService('drive')
    context = {'uploaded': 'true'}

    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            #Save the file to disk
            with open('./uploaded.pdf', 'wb+') as destination:
                for chunk in request.FILES['uploadedFile'].chunks():
                    destination.write(chunk)
            #Create File Metadata
            fileMetaData = { 'name' : form.cleaned_data['name'].studentName + '.pdf' }
            #Create Uploadable File Pointer
            media = MediaFileUpload('./uploaded.pdf',mimetype='application/pdf')
            #Upload
            file = service.files().create(body=fileMetaData,media_body=media,fields='id').execute()
            #If Uploaded, Delete File on Disk
            if(file.get('id') != 'null'):
                os.remove('./uploaded.pdf')
            
            return render(request, './index.html', context)
    else:
        form = UploadFileForm()
        
    return render(request, './index.html', {'form': form})

