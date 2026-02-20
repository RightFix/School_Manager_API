from django.urls import path
from .views import register_student, grade

urlpatterns =[
 path('register/', register_student, name='register_student'),
 path('grade/', grade, name='grade'),
 
]