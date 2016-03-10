from django.shortcuts import render, redirect
from courses.models import Lesson
from courses.models import Course
from students.models import Student
from django.shortcuts import render_to_response
import datetime
from students.forms import StudentModelForm
from django.contrib import messages


def list_view(request):
    try:
        cid = int(request.GET.get('course_id', '')[0])
        students = Student.objects.filter(courses=cid)
        return render(request, 'students/list.html', {'students': students})
    except IndexError:
        my_list = ['python', 'html', 'javascript']
        students = Student.objects.all()
        return render(request, 'students/list.html', {'students': students, 'my_list': my_list})


def detail(request, item_id):
    students = Student.objects.all()
    student = Student.objects.get(id=item_id)
    return render(request, 'students/detail.html', {'student': student})


def create(request):
    if request.method == 'POST':
        model_form = StudentModelForm(request.POST)
        if model_form.is_valid():
            student = model_form.save()
            messages.success(request, 'Student %s %s has been successfully added' % (student.name, student.surname)) 
            return redirect('students:list_view')
    else:
        model_form = StudentModelForm()
    return render(request, 'students/add.html', {'model_form': model_form})


def edit(request, item_id):
    application = Student.objects.get(id=item_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Info on the student has been sucessfully changed.')
    else:
        form = StudentModelForm(instance=application)
    return render(request, 'students/edit.html', {'form': form})


def remove(request, item_id):
    application = Student.objects.get(id=item_id)
    if request.method == 'POST':
        form = StudentModelForm(request.POST, instance=application)
        obj = form.instance
        application.delete()
        messages.success(request, 'Info on %s %s has been sucessfully deleted.' % (obj.name, obj.surname))
        return redirect('students:list_view')

    return render(request, 'students/remove.html')






# Create your views here.
