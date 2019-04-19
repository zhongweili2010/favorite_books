######login views##########
from django.shortcuts import render,redirect
from . import views
from .models import User
from django.contrib import messages
# Create your views here.

def login_and_registration(request):

    return render(request,'login_registration_app/index.html')

def login(request):
    if request.method=="POST":
        error=User.objects.login(request.POST)
        if len(error)==0:
            x = User.objects.get(email=request.POST['email'])
            request.session['name']=f"{x.first_name} {x.last_name}"
            request.session['id']=x.id
            return redirect('/books')
        else:
            for key,value in error.items():
                print(value)
                messages.info(request,value,extra_tags=key)
            return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')


def register(request):
    if request.method=="POST":
        errors=User.objects.validate(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                print(value)
                messages.info(request,value,extra_tags=key)
            return redirect('/')
        else:
            x=User.objects.get(email=request.POST['email'])
            print(f"XXXXXXXXX id is {x.id}")
            return redirect('/')



def success(request):
    if 'name' in request.session:
        return render(request,'login_registration_app/success.html')
    else:
        return redirect('/')

