from django.contrib import admin
from .models import Faculty, FieldOfStudy, Term


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(FieldOfStudy)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(Term)
class FacultyAdmin(admin.ModelAdmin):
    pass

# admin.site.register(Term)