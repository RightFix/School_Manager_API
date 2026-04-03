from django.contrib import admin
from .models import Teacher, Student, Grade, Course, Enrollment


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    search_fields = (
        "employee_id",
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    list_display = ("employee_id", "user", "phone", "created_at")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ("reg_no", "user__username", "user__first_name", "user__last_name")
    list_display = ("reg_no", "user", "phone", "parent_name", "created_at")


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    search_fields = ("student__reg_no", "subject", "grade")
    list_display = ("student", "subject", "grade", "created_at")
    list_filter = ("subject", "grade")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("name", "code")
    list_display = ("name", "code", "teacher", "created_at")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    search_fields = ("student__reg_no", "course__name")
    list_display = ("student", "course", "enrolled_at")
