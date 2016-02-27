from django.shortcuts import render
from courses.models import Lesson
from courses.models import Course
from django.shortcuts import render_to_response


def detail(request, item_id):
    courses = Course.objects.filter(id=item_id)
    course = Course.objects.get(id=item_id)

    lessons_all = Lesson.objects.filter(course=courses)
 
    return render_to_response('courses/detail.html', {'courses': courses, 'lessons_all': lessons_all, 'particular_course':course.id, 'course':course})
