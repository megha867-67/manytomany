from django.shortcuts import render,redirect
from .models import Student,Course
from .forms import CourseForm,StudentForm

def insertcourse(request):

    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('insertcourse')

    else:
        form = CourseForm()

    return render(request, 'insertcourse.html',
                  {'form': form})

def insertstudent(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('studentlist')

    else:
        form = StudentForm()

    return render(request, 'insertstudent.html',
                  {'form': form})
def studentlist(request):
    students=Student.objects.prefetch_related('courses').all()
    return render (request,'studentlist.html',{'students':students})
# Create your views here.
