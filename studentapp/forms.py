from django import forms
from .models import Course,Student
class CourseForm(forms.ModelForm):
    class Meta:
       model=Course
       fields=['coursename']
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['studentname','courses']
        widgets={
        'courses':forms.CheckboxSelectMultiple()
        }