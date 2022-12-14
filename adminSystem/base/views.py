from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from base.EmailBackEnd import EmailBackEnd
from django.contrib import messages



# Create your views here.

def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect("/")
            else:
               return HttpResponseRedirect("/")
        else:
            messages.error(request,"Invalid Login Details")
            return HttpResponseRedirect("/")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")




