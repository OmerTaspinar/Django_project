from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("detail",views.detail,name="detail"),
    path("lists",views.lists,name="lists"),
    path("student",views.student,name="student"),
    path("academician",views.academician,name="academician"),
    path("<int:department",views.getAcademicianDepartmentID),
    path("<str:department>",views.getAcademicianDepartment,name="department_of_academician"),
    
]
