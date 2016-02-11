from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from . import views

#def quadratic(request):
#    a = request.GET['a']
#   print a, type(a)
#    b = request.GET['b']
#    print b, type(b)
#    c = request.GET['c']
#    d = b**2 - 4*a*c
#    print d
#    print c, type(c) 
#    return render_to_response('results.html', {'a':a, 'b':b, 'c':c})


urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_list/$', views.student_list, name='student_list'),
    url(r'^student_detail/$', views.student_detail, name='student_detail'),
#    url(r'^quadratic/results/$', quadratic, name='quadratic'),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'sdacademy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
