from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Profile, Grade

# Create your views here.

def register_student(request):
    student = request.GET.get('student')

    check = Profile.objects.filter(reg_no = student.upper())

    if student and not check:
        Profile.objects.create(reg_no= student.upper())
        return HttpResponse("Profile Created")

    if check:
        return HttpResponse("Profile Already Created")

    else:
        return HttpResponse("Error During Creation")


def grade(request):
    student = request.GET.get('student')
    math= request.GET.get('math').upper()
    english= request.GET.get('english').upper()
    physics= request.GET.get('physics').upper()
    chemistry= request.GET.get('chemistry').upper()

    check = Profile.objects.filter(reg_no = student.upper())
    print(student.upper())

    if check:
        Grade.objects.create(student_id= student, math= math, english= english,  chemistry= chemistry, physics= physics)
        return HttpResponse("Student Result Uploaded Succesfully")
        
    
    else:
        return HttpResponse("Student is not registed yet")