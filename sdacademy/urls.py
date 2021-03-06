from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.http import HttpResponse
from . import views
#from courses import views
#from quadratic import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
#    url(r'^student_list/$', views.student_list, name='student_list'),
#    url(r'^student_detail/$', views.student_detail, name='student_detail'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^quadratic/', include('quadratic.urls')),
    url(r'^courses/', include('courses.urls', namespace="courses", app_name="courses")) ,
    url(r'^students/', include('students.urls', namespace="students", app_name="students")) ,
    url(r'^coaches/', include('coaches.urls', namespace="coaches", app_name="coaches")) ,
	url(r'', include('feedbacks.urls', app_name="feedbacks")) ,
)
