from django.shortcuts import render
from feedbacks.models import Feedback
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.core.mail import mail_admins
from django.contrib import messages


class FeedbackView(CreateView):
    model = Feedback
    success_url = reverse_lazy('feedback')
    template_name = 'feedbacks/feedback.html'
    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Feedback"
        return context
    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        print subject
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        mail_admins(subject, message)
        messages.success(self.request, ('Thank you for your feedback! We will keep in touch with you very soon!'))
        return super(FeedbackView, self).form_valid(form)

# Create your views here.
