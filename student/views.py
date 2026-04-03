from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Teacher, Student, Grade, Course, Enrollment
from .serializers import (
    UserSerializer,
    TeacherSerializer,
    StudentSerializer,
    GradeSerializer,
    CourseSerializer,
    EnrollmentSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        user_data = request.data.pop("user", None)
        if user_data:
            user = User.objects.create_user(
                username=user_data.get("username"),
                email=user_data.get("email", ""),
                password=user_data.get("password", ""),
                first_name=user_data.get("first_name", ""),
                last_name=user_data.get("last_name", ""),
            )
            teacher = Teacher.objects.create(user=user, **request.data)
        else:
            teacher = Teacher.objects.create(**request.data)
        serializer = self.get_serializer(teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        user_data = request.data.pop("user", None)
        if user_data:
            user = User.objects.create_user(
                username=user_data.get("username"),
                email=user_data.get("email", ""),
                password=user_data.get("password", ""),
                first_name=user_data.get("first_name", ""),
                last_name=user_data.get("last_name", ""),
            )
            student = Student.objects.create(user=user, **request.data)
        else:
            student = Student.objects.create(**request.data)
        serializer = self.get_serializer(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["get"], url_path="student/(?P<student_id>[^/]+)")
    def by_student(self, request, student_id=None):
        grades = Grade.objects.filter(student_id=student_id)
        serializer = self.get_serializer(grades, many=True)
        return Response(serializer.data)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["get"], url_path="student/(?P<student_id>[^/]+)")
    def by_student(self, request, student_id=None):
        enrollments = Enrollment.objects.filter(student_id=student_id)
        serializer = self.get_serializer(enrollments, many=True)
        return Response(serializer.data)
