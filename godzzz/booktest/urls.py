from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    #url(r'^HelloWorld$', views.HelloWorld)
    url(r'^\d+', views.HelloWorld),
    url(r'^static', views.Static),
]
