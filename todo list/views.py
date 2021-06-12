from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from todo_list import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def userlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return HttpResponseRedirect('/todo_list/todo_list')
        else:
            res=render(request,'todo_list/todo_login.html',{'error':"Username and password is incorrect"})
            return res
    else:
        return render(request,'todo_list/todo_login.html')



def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/todo_list/login_todo/')



@login_required(login_url="/todo_list/login_todo/")
def todo_list(request):
    res=render(request,'todo_list/todo1.html')
    return res

@login_required(login_url="/todo_list/login_todo/")
def add_list(request):
    if request.method=="POST":
        todo = models.Todouser()
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.save()
        return HttpResponseRedirect("/todo_list/todo_list/")
