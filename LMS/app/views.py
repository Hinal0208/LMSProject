from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def Dashboard(request):
    return render (request,'dashboard.html')

    

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/dashboard.html')
        else:
            return HttpResponseRedirect ("/dashboard")

    return render (request,'login.html')

def Homebtn(request): 
    return HttpResponseRedirect(request,'homebtn.html')




    

