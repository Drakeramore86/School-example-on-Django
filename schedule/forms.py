from django import forms
from .models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    q = forms.CharField(max_length=255)


class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
