from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.contrib import messages
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from itertools import chain
# import random

from .forms import RegisterForm

def index(request):
  if request.method=='POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    if username and password:
      user=authenticate(username=username,password=password)
      print(username,password)
      print(user)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.error(request,'Username or Password is Incorrect')
    else:
      messages.error(request,'Fill out all the fields')
  
  return render(request,'core/signin.html',{})


def registerUser(request):
  print("CCCCCCCCCCC1")
  form=RegisterForm()
  print(request.method)
  if request.method=='POST':
    print("CCCCCCCCCCCCCCC2")
    form=RegisterForm(request.POST)
    if form.is_valid():
      print("CCCCCCCCCCCCCCCCCCCCCC3")
      form.save()
      # return redirect('signin')
      return render(request,'core/signin.html',{})
  # else:
  #   form=RegisterForm()
  return render(request,'core/signup.html',{'form':form})


def loginUser(request):
  # print("CCCCCCCCCCCCCCCCC1")
  if request.method=='POST':
    # print("CCCCCCCCCCCCCCCCC2")
    username=request.POST.get('username')
    password=request.POST.get('password')
    # print("CCCCCCCCCCCCCCCCC3")
    # print(emailaddress,password)
    if username and password:
      user=authenticate(username=username,password=password)
      print(username,password)
      print(user)
      if user is not None:
        login(request,user)
        return redirect('home')
      else:
        messages.error(request,'Username or Password is Incorrect')
    else:
      messages.error(request,'Fill out all the fields')
  
  return render(request,'core/signin.html',{})

def home(request):
  return render(request,'core/homepage.html',{})

def profiles(request):
  return render(request,'core/profiles.html',{})

def jobboards(request):
  return render(request,'core/jobboards.html',{})

def eventlistings(request):
  return render(request,'core/eventlistings.html',{})

def joblisitings(request):
  return render(request,'core/joblistings.html',{})

def connections(request):
  return render(request,'core/connections.html',{})
