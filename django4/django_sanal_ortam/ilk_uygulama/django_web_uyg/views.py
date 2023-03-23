from django.shortcuts import render,redirect
from django.http.response import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from datetime import datetime
# Create your views here.
data={
    "MechatronicEng":['Automotive Control','Signal Processing','Mechatronic Design'],
    "ElectricalEng":['Electrical','Circuits and Systems Theory','Control and Control Systems'],
    "ComputerEng":['Network Systems','Embedded Systems','Operating Systems'],
    "SoftwareEng":['IT','Software','Database'],
    "MechanicalEng":['Hydromechanical and Hydraulic Machines','Machine Theory','Automotive'],
    

}







def index(request):
    # return HttpResponse(f"<h1>Hello! Ömer</h2>")
    lists_oge=" "
    department_list=list(data.keys())

    for department in department_list:
        redirect_path = reverse("department_of_academician",args=[department])
        lists_oge+=f"<li><a href=\"{redirect_path}\" >{department}</a></li>"

    html=f"<ul>{lists_oge}</ul>"
    # return HttpResponse(html)
    return render(request,"index.html",{
        "departments":department_list
    })
def detail(request):
    return HttpResponse(f"<h2>Welcome to detail page.</h2>")
def lists(request):
    return HttpResponse(f"<h2>Welcome to list page.</h2>")
def student(request):
    return HttpResponse("Student Page")
def academician(request):
    return HttpResponse("Academician Page")

def getAcademicianDepartment(request,department):
# These are not useable method    
#     department_text=None
#     if deparment=="MEE":
#         department_text="Academician in Mechatronic engineering"
#     elif department=="EE":
#         department_text="Academician in Electrical engineering"
#     else:
#         department_text="Academician of another department"
#     return HttpResponse(bolum_text)                     


    try:
        department_text=data[department]
        dimension=len(department_text)
        things="Python"
        things2="Django Rest Framework"
        # return HttpResponse(f"<h1>{department_text}</h1>")
        return render(request,"departmentList.html",{
            "department":department,
            "department_text":department_text,
            "lenght":dimension,
            "things":things,
            "things2":things2,
            "now":datetime.now()

        })
    except:
        return HttpResponseNotFound(f"<h1>Wrong Page.</h1>")

def getAcademicianDepartmentID(request,department):
    department_list=list(data.keys())

    if department > len(department_list):
        return HttpResponseNotFound(f"<h1>Wrong Page</h1>")
    department_name = department_list[department-1]
    redirect_path=reverse("department_of_academician",args=[department_name])

    return redirect(redirect_path)