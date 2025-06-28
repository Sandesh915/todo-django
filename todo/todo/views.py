from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import models
from .models import TODO
from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.decorators import login_required

# Create your views here.
            

def signup(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        myuser = User.objects.create_user(fnm, emailid, pwd)
        myuser.save()
        return redirect('loginn')
    return render(request, 'signup.html')


def loginn(request):
    if request.method == "POST":
        fnm = request.POST.get('fnm')           # This is your "username"
        pwd = request.POST.get('pwd')           # This is your "password"
        
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('/todopage')        # Redirect after login
        else:
            return render(request, 'loginn.html', {'error': 'Invalid credentials'})
    
    return render(request, 'loginn.html')


@login_required(login_url='loginn')
def todo(request):
    if request.method == "POST":
        title = request.POST.get('task')
        if title:  
            obj = TODO(title=title, user=request.user)
            obj.save()
        res = TODO.objects.filter(user=request.user).order_by('-date')
        return render(request, 'todo.html', {'res': res, 'user': request.user.username})
    res = TODO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res, 'user': request.user.username})


@login_required(login_url='loginn')
def edit_todo(request, srno):
    if request.method == "POST":
        title = request.POST.get('task')
        if title:  
            obj = TODO.objects.get(srno=srno)
            obj.title = title
            obj.save()
        return redirect('todopage')  # Redirect to the todo page
    
    obj = TODO.objects.get(srno=srno)
    return render(request, 'todo.html', {'obj': obj})


@login_required(login_url='loginn')
def delete_todo(request, srno):
    obj = TODO.objects.get(srno=srno)
    obj.delete()
    return redirect('todopage')  # Redirect to the todo page


def signout(request):
    logout(request)
    return redirect('loginn')