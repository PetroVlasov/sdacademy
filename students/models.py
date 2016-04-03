from django.db import models
from courses.models import Course
from django.core.urlresolvers import reverse_lazy, reverse


class Student(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    skype = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)

    def __unicode__(self):
        return self.name

    def full_name(self):
        return '%s %s' % (self.name, self.surname) 
	
#    def get_absolute_url(self):
#        return reverse('students:edit', current_app='student', kwargs={'pk': self.object.pk})

# Create your models here.
