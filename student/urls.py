from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    TeacherViewSet,
    StudentViewSet,
    GradeViewSet,
    CourseViewSet,
    EnrollmentViewSet,
)

router = DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"students", StudentViewSet)
router.register(r"grades", GradeViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
