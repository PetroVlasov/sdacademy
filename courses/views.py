from django.shortcuts import render, redirect
from courses.models import Lesson
from courses.models import Course
from courses.forms import CourseModelForm, LessonModelForm
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse



class CourseDetailView(DetailView):
    model = Course
    template_name= 'courses/detail.html'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        pk = self.get_object().pk
        courses = Course.objects.filter(pk=pk)
        lessons_all = Lesson.objects.filter(course=courses)
        context['lessons_all'] = lessons_all
        return context

class CourseCreateView(CreateView):
    model = Course
    success_url = reverse_lazy('index')
    template_name= 'courses/add.html'
    def get_context_data(self, **kwargs):
        context = super(CourseCreateView, self).get_context_data(**kwargs)
        context['title'] = "Course creation"
        return context
    def form_valid(self, form):
        messages.success(self.request, ('Course %s has been successfully added.' % form.instance.name))
        return super(CourseCreateView, self).form_valid(form)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/edit.html'
    def get_context_data(self, **kwargs):
        context = super(CourseUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Course update"
        return context
    def form_valid(self, form):
        messages.success(self.request, 'The changes have been saved.')
        return super(CourseUpdateView, self).form_valid(form)
    def get_success_url(self):
        return reverse('courses:course-edit', kwargs={'pk': self.object.pk})


class CourseDeleteView(DeleteView):
    model = Course
    template_name= 'courses/remove.html'
    def get_context_data(self, **kwargs):
        context = super(CourseDeleteView, self).get_context_data(**kwargs)
        title = "Course deletion"
        context['title'] = title       
        return context
    def get_success_url(self):
        course = super(CourseDeleteView, self).get_object()
        message = ('Course %s has been deleted.' % (course.name))
        messages.success(self.request, message)
        return reverse('index')


def add_lesson(request, pk):
    courses = Course.objects.filter(pk=pk)
    course = Course.objects.get(pk=pk)
    lessons_all = Lesson.objects.filter(course=courses)
 
    if request.method == 'POST':
        
        model_form = LessonModelForm(request.POST)
        
        if model_form.is_valid():
            lesson = model_form.save()
            messages.success(request, 'Lesson %s has been successfully added.' % lesson.subject) 
            return redirect('courses:detail', pk=pk)
    else:
        model_form = LessonModelForm(initial={"course": pk})
    return render(request, 'courses/add_lesson.html', {'model_form': model_form})    


