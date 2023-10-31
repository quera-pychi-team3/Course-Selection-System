from django.contrib import admin
from .models import *


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    pass


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(FieldOfStudy)
class FieldOfStudyAdmin(admin.ModelAdmin):
    pass

#
# admin.site.register(FieldOfStudy)
# admin.site.register(Term)
# admin.site.register(Faculty)
