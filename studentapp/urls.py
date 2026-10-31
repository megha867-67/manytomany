from django.urls import path
from . import views

urlpatterns = [

    path('', views.insertcourse,
         name='insertcourse'),

    path('insertstudent', views.insertstudent,
         name='insertstudent'),

    path('students', views.studentlist,
         name='studentlist'),

]