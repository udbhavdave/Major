from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
import pytesseract
from pytesseract import Output
import cv2
import os
# Create your views here.

# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'

def index(request):
    # return HttpResponse("Hello World")
    pics = Image.objects.all()
    return render(request, 'search/index.html', {
        "upload": UploadForm(),
        "search": SearchForm(),
        "pics": pics
    })

def upload(request):
    if request.method == "POST":
        # print(request.FILES)
        form=UploadForm(request.POST, request.FILES)
        # uploaded_file=request.FILES['upload']
        # fs=FileSystemStorage()
        # name=fs.save(uploaded_file.name,uploaded_file)
        # print(uploaded_file.name,uploaded_file.size,fs.url())
        if form.is_valid():
            # print(form.cleaned_data)
            image_name = form.cleaned_data["upload"]
            image=Image.objects.create(image_name=image_name)
            path='smartdoc'+image.image_name.url
            # print(path,image.image_name.path)
            text = pytesseract.image_to_string(path)
            image.text=text
            image.save()
            return HttpResponseRedirect(reverse('index'))
            # print(image.image_name.url,image.image_name,text)
    return HttpResponseRedirect(reverse('index'))

def search(request):
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            search_text=form.cleaned_data["search"]
            print(search_text)
            pics = Image.objects.filter(text__icontains=search_text)
            context={'pics':pics,
            "upload": UploadForm(),
            "search": form,}
            return render(request, 'search/index.html', context)
    return HttpResponseRedirect(reverse('index'))