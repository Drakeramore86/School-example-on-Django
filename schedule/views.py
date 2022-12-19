from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .models import Course, Teacher, Student
from .forms import SearchForm
from django.urls import reverse
from django import views
from django.contrib.auth.views import LoginView


# Create your views here.
def main(request):
    if request.method == 'GET':
        query = SearchForm(request.GET)
        if query.is_valid():
            courses = Course.objects.filter(title__contains=request.GET.get('q'))

        else:
            courses = Course.objects.all()
    return render(request, 'schedule/main.html', context={
        'courses': courses
    })


class CourseView(views.View):
    def get(self, request, course_id):
        template_name = 'schedule/courses.html'
        course = Course.objects.get(id=course_id)
        test = Student.objects.all()
        students = test.filter(course=course_id)
        return render(request, template_name, {'course': course, "students": students})


class TeacherView(views.View):
    def get(self, request, teacher_id):
        template_name = 'schedule/teachers.html'
        teacher = Teacher.objects.get(id=teacher_id)
        return render(request, template_name, {'teacher': teacher})


class AddCourseView(CreateView):
    model = Student
    fields = '__all__'
    success_url = "/schedule/add_course/"

    def get_success_url(self):
        return reverse('add_course')


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/schedule/main'
    template_name = 'signup.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
