from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def HelloWorld(request):
    list = BookInfo.objects.all()

    return render(request,'booktest/HelloWorld.html',{'list':list})
def Static(request):
    return render(request,'booktest/Static.html')
