from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^index/$', views.index,name='index'),
    url(r'^board/$', views.board,name='board'),

]