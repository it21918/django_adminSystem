from contextlib import nullcontext
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from base.models import CustomUser

def admin_home(request):
    users=CustomUser.objects.all()
    return render(request,"admin_templates/admin_home.html",{"users":users})

def edit_user(request,user_id):
    user=CustomUser.objects.get(id=user_id)
    return render(request,"admin_templates/edit_user.html",{"user":user,"id":user_id})

def edit_user_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user_id=request.POST.get("id")
        user_type = request.POST.get("user_type")
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email = request.POST.get("email")
        is_staff = request.POST.get("is_staff")
        is_active = request.POST.get("is_active")
        is_superuser=request.POST.get("is_superuser")

        try:
            user=CustomUser.objects.get(id=user_id)
            user.id = user_id
            user.is_superuser = is_superuser
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = user.email
            user.is_staff = user.is_staff
            user.is_active = user.is_active
            user.user_type = user_type
            user.save()

            messages.success(request,"Successfully Edited user")
            return HttpResponseRedirect(reverse("edit_user",kwargs={"user_id":user_id}))
        except:
            messages.error(request,"Failed to Edit user" )
            return HttpResponseRedirect(reverse("edit_user",kwargs={"user_id":user_id}))

def add_user(request):
    return render(request,"admin_templates/add_user.html")

def add_user_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        user_type = request.POST.get("user_type")
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email = request.POST.get("email")
        is_staff = request.POST.get("is_staff")
        is_active = request.POST.get("is_active")
        is_superuser=request.POST.get("is_superuser")
        password= request.POST.get("password")
        try:
            user=CustomUser.objects.create_user(
                user_type = user_type,
                username = username,
                last_name=last_name,
                first_name=first_name,
                email=email,
                password=password,
                is_staff = is_staff,
                is_active = is_active,
                is_superuser = is_superuser
            )
            user.save()
            
            messages.success(request,"Successfully Added user")
            return HttpResponseRedirect(reverse("add_user"))
        except:
            messages.error(request,"Failed to Add user")
            return HttpResponseRedirect(reverse("add_user"))

def delete_user(request,user_id):
    try:
        user=CustomUser.objects.get(id=user_id)
        user.delete()
                
        messages.success(request,"Successfully deleted user")
        return HttpResponseRedirect(reverse("admin_home"))
    except:
        messages.error(request,"Failed to delete user")
        return HttpResponseRedirect(reverse("admin_home"))
