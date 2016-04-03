from django.conf.urls import patterns, include, url
from django.shortcuts import render
from . import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/add_lesson$', views.add_lesson, name="add-lesson"),
    url(r'^add/$', views.CourseCreateView.as_view(), name="course-add"),
    url(r'^edit/(?P<pk>\d+)/$', views.CourseUpdateView.as_view(), name="course-edit"),
    url(r'^remove/(?P<pk>\d+)/$', views.CourseDeleteView.as_view(), name='course-remove'),
)
