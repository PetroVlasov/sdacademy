from django.shortcuts import render
from courses.models import Lesson
from courses.models import Course
from students.models import Student
from django.shortcuts import render_to_response


def list_view(request):
    try:
        cid = int(request.GET.get('course_id', '')[0])
        students = Student.objects.filter(courses=cid)
        return render(request, 'students/list.html', {'students': students})
    except IndexError:
        students = Student.objects.all()
        return render(request, 'students/list.html', {'students': students})

def detail(request, item_id):
    students = Student.objects.all()
    student = Student.objects.get(id=item_id)
    print student.surname
    return render(request, 'students/detail.html', {'student': student})
# Create your views here.
