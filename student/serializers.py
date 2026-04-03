from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teacher, Student, Grade, Course, Enrollment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]
        read_only_fields = ["id"]


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user",
            "user_id",
            "employee_id",
            "phone",
            "address",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "user_id",
            "reg_no",
            "phone",
            "address",
            "date_of_birth",
            "parent_name",
            "parent_phone",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class GradeSerializer(serializers.ModelSerializer):
    student_reg_no = serializers.CharField(source="student.reg_no", read_only=True)

    class Meta:
        model = Grade
        fields = [
            "id",
            "student",
            "student_reg_no",
            "subject",
            "grade",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class CourseSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(
        source="teacher.user.get_full_name", read_only=True
    )

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "code",
            "description",
            "teacher",
            "teacher_name",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


class EnrollmentSerializer(serializers.ModelSerializer):
    student_reg_no = serializers.CharField(source="student.reg_no", read_only=True)
    course_name = serializers.CharField(source="course.name", read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_reg_no",
            "course",
            "course_name",
            "enrolled_at",
        ]
        read_only_fields = ["id", "enrolled_at"]
