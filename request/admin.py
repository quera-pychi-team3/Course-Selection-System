from django.contrib import admin
from django.contrib.auth.models import Group
from request.models.registration import Registration
from request.models.registration_update import RegistrationUpdate
from request.models.course_drop import CourseDrop
from request.models.term_drop import TermDrop
from request.models.review_grade import ReviewGrade
from request.models.enrollment_verification import EnrollmentVerification

admin.site.unregister(Group)


admin.site.register(Registration, admin.ModelAdmin)
admin.site.register(RegistrationUpdate, admin.ModelAdmin)
admin.site.register(CourseDrop, admin.ModelAdmin)
admin.site.register(TermDrop, admin.ModelAdmin)
admin.site.register(ReviewGrade, admin.ModelAdmin)
admin.site.register(EnrollmentVerification, admin.ModelAdmin)

