from django.contrib import admin
from .models import Course, TermCourse, StudentCourse

admin.site.register(Course, admin.ModelAdmin)
admin.site.register(TermCourse, admin.ModelAdmin)
admin.site.register(StudentCourse, admin.ModelAdmin)