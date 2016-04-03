from courses.models import Lesson, Course
from students.models import Student
import datetime
from students.forms import StudentModelForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse


class StudentListView(ListView):
    model = Student
    paginate_by = 2
    def get_queryset(self):
        course_id= self.request.GET.get('course_id', None)
        if course_id:
            students = Student.objects.filter(courses=course_id)
        else:
            students = Student.objects.all()
        return students
    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        course_id= self.request.GET.get('course_id', None)
        context['course_id'] = course_id
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    def get_context_data(self, **kwargs):
        context = super(StudentCreateView, self).get_context_data(**kwargs)
        context['title'] = "Student registration"
        return context
    def form_valid(self, form):
        messages.success(self.request, ('Student %s %s has been successfully added' % (form.instance.name, form.instance.surname)))
        return super(StudentCreateView, self).form_valid(form)


class StudentUpdateView(UpdateView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Student info update"
        return context
    def form_valid(self, form):
        messages.success(self.request, 'Info on the student has been sucessfully changed.')
        return super(StudentUpdateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('students:edit', kwargs={'pk': self.object.pk})


class StudentDeleteView(DeleteView):
    model = Student
    def get_context_data(self, **kwargs):
        context = super(StudentDeleteView, self).get_context_data(**kwargs)
        title = "Student info suppression"
        context['title'] = title
        return context
    def get_success_url(self):
        student = super(StudentDeleteView, self).get_object()
        message = ('Info on %s %s has been sucessfully deleted.' % (student.name, student.surname))
        messages.success(self.request, message)
        return reverse('students:list_view')
        

