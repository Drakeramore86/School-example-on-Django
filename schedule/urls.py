from django.urls import path, include
from .views import main, CourseView, TeacherView, AddCourseView, MySignupView, MyLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('schedule/main/', main, name='main'),
    path('schedule/course_details/<int:course_id>/', CourseView.as_view()),
    path('schedule/teacher_details/<int:teacher_id>/', TeacherView.as_view()),
    path('schedule/add_course/', AddCourseView.as_view(), name='add_course'),
    path('signup/', MySignupView.as_view()),
    path('login/', MyLoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]