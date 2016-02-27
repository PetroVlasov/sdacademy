# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render

def quadratic(request):
    context={}
    a = context['a'] = request.GET.get('a','')
    b = context['b'] = request.GET.get('b','')
    c = context['c'] = request.GET.get('c','')

    try:
        a = int(a)
        if a == 0:
            context['zeroa'] = "коэффициент при первом слагаемом уравнения не может быть равным нулю"
    except ValueError:
        if str(a):
            context['nonemptya'] = "коэффициент не целое число"
        else:
            context['emptya'] = "коэффициент не определен"
    
    try:
        b = int(b)
    except ValueError:
        if str(b):
            context['nonemptyb'] = "коэффициент не целое число"
        else:
            context['emptyb'] = "коэффициент не определен"

    try:
        c = int(c)
    except ValueError:
        if str(c):
            context['nonemptyc'] = "коэффициент не целое число"
        else:
            context['emptyc'] = "коэффициент не определен"

    try:
        context['d'] = float(b)**2 - 4*float(a)*float(c)
        d = context['d']
        if d > 0 and a != 0:
            context['descr'] = 'Дискриминант: %d' %d
            context['x1'] = (-float(b) + float(d) ** (1/2.0)) / 2*float(a)
            context['x2'] = (-float(b) - float(d) ** (1/2.0)) / 2*float(a)
            print context['x2']
            print context['x1']
            context['result'] = "Квадратное уравнение имеет два действительных корня: x1 = %s, x2 = %s" % (context['x1'] + 0, context['x2'] + 0) 
        elif d < 0:
            context['descr'] = 'Дискриминант: %d' %d
            context['result'] = "Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений."
        elif d == 0 and a != 0:
            context['descr'] = 'Дискриминант: %d' %d
            context['x1'] = (-float(b) + float(d) ** (1/2.0)) / 2.0*float(a)
            context['result'] = "Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %s" % (context['x1'] + 0)      
    except ValueError:
        context['error'] = "error"

    return render(request, 'results.html', context)

# Create your views here.