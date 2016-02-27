from django.conf.urls import patterns, include, url
from django.shortcuts import render
from . import views

urlpatterns = patterns('',
    url(r'^$', views.list_view, name='list_view'),   
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
)
