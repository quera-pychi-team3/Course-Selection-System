from django.contrib import admin
from django.contrib.auth.models import Group
from requests.models import registration, registration_update, course_drop, term_drop, review_grade, enrollment_verification

admin.site.unregister(Group)


@admin.register(registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('student', 'courses', 'approval_status')


@admin.register(registration_update)
class RegistrationUpdateAdmin(admin.ModelAdmin):
    list_display = ('student', 'add_courses', 'del_courses', 'approval_status')


@admin.register(course_drop)
class CourseDropAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'student_description', 'educational_deputy_description')


@admin.register(term_drop)
class TermDropAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'student_description', 'educational_deputy_description')


@admin.register(review_grade)
class ReviewGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'review_text', 'result_text')


@admin.register(enrollment_verification)
class EnrollmentVerificationAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrollment_verification_file', 'term', 'issuance_certificate_place')