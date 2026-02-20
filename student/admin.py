from django.contrib import admin
from .models import Profile, Grade
# Register your models here.

admin.site.register([Profile, Grade])

class ProfileAdmin(Profile):
    search_fields = ("reg_no",)
    list_display = ('reg_no', 'created_at')
    list_filter = ('created_at',)


class GradeAdmin(Grade):
    list_display = ('student_id', 'math', 'english', 'physics', 'chemistry')
    search_fields= ('student_id', 'math', 'english', 'physics', 'chemistry')
    list_filter = ('math', 'english', 'physics', 'chemistry')
    list_editable =('math', 'english', 'physics', 'chemistry')