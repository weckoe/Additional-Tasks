from django.contrib import admin

from . import models


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'grade', 'gpa']
