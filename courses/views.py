from django.shortcuts import render, redirect
from courses.models import Lesson
from courses.models import Course
from django.shortcuts import render_to_response
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages


def detail(request, item_id):
    courses = Course.objects.filter(pk=item_id)
    course = Course.objects.get(pk=item_id)

    lessons_all = Lesson.objects.filter(course=courses)
 
    return render(request, 'courses/detail.html', {'courses': courses, 'lessons_all': lessons_all, 'particular_course':course.id, 'course':course})


def add(request):
    if request.method == 'POST':
        model_form = CourseModelForm(request.POST)
        if model_form.is_valid():
            course = model_form.save()
            messages.success(request, 'Course %s has been successfully added.' % course.name) 
            return redirect('index')
    else:
        model_form = CourseModelForm()
    return render(request, 'courses/add.html', {'model_form': model_form})    


def edit(request, item_id):
    application = Course.objects.get(pk=item_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=application)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'The changes have been saved.')
    else:
        form = CourseModelForm(instance=application)
    return render(request, 'courses/edit.html', {'form': form})


def remove(request, item_id):
    application = Course.objects.get(pk=item_id)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=application)
        obj = form.instance
        application.delete()
        messages.success(request, 'Course %s has been deleted.' % (obj.name))
        return redirect('index')

    return render(request, 'courses/remove.html')

def add_lesson(request, item_id):
    courses = Course.objects.filter(pk=item_id)
    course = Course.objects.get(pk=item_id)
    print course.coach
    print course.assistant
    lessons_all = Lesson.objects.filter(course=courses)
 
    if request.method == 'POST':
        
        model_form = LessonModelForm(request.POST)
        
        if model_form.is_valid():
            lesson = model_form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson.subject) 
            return redirect('courses:detail', item_id=item_id)
            #return render(request, 'courses/detail.html', {'lessons_all': lessons_all, 'course':course})
    else:
        model_form = LessonModelForm(initial={"course": item_id})
    return render(request, 'courses/add_lesson.html', {'model_form': model_form})    


