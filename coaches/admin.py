from django.contrib import admin
from coaches.models import Coach
from django.contrib.auth.models import User


class CoachAdmin(admin.ModelAdmin):
    list_display = ['get_first_name', 'get_last_name', 'gender', 'skype', 'description']
    list_filter = ['user__is_staff']

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_is_staff(self, obj):
        return obj.user.is_staff

admin.site.register(Coach, CoachAdmin)

# Register your models here.
