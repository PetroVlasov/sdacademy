from django.conf.urls import patterns, include, url
from django.shortcuts import render
from . import views

urlpatterns = patterns('',
    url(r'^(?P<item_id>\d+)/$', views.detail, name="detail"),
    url(r'^(?P<item_id>\d+)/add_lesson$', views.add_lesson, name="add-lesson"),
    url(r'^add/$', views.add, name="course-add"),
    url(r'^edit/(?P<item_id>\d+)/$', views.edit, name="course-edit"),
    url(r'^remove/(?P<item_id>\d+)/$', views.remove, name='course-remove'),
)
