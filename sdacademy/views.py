from django.shortcuts import render
from django.shortcuts import render_to_response
from courses.models import Course
from courses.models import Lesson


def index(request):
    courses_all = Course.objects.all()
    return render_to_response('index.html', {'courses_all': courses_all})

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')
    
def contact(request):
    return render(request, 'contact.html')


