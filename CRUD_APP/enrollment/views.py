from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
from django.contrib.auth import hashers

# Create your views here.
def add_view(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=hashers.make_password(fm.cleaned_data['password'])
            reg=User(name=nm,email=em,password=pwd)
            reg.save()
            fm=StudentRegistration()
            
            
    else:
        fm=StudentRegistration()
    stu=User.objects.all()
    return render(request, 'enroll/addandviewstudents.html', {"form":fm, "stu":stu})

def update_student(request, id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudents.html', {'form':fm})

# this function is to delete student record on its id
def delete(request, id):
    if request.method=="POST":
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")