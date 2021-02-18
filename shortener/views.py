from django.shortcuts import render, redirect
import uuid
from .models import urlinks
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shortener/index.html')

def create(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = urlinks(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_details = urlinks.objects.get(uuid=pk)
    return redirect(url_details.link)





