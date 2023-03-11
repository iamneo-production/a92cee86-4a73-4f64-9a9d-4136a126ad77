from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from itertools import chain
import random
# from django.http import HttpResponse
# from django.contrib.auth.decorators import login_required
# from itertools import chain
# import random

from .forms import RegisterForm



@login_required(login_url='signin')
def index(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Credentials Invalid')
        return redirect('signin')

  else:
    return render(request, 'core/signin.html')
    # user_object = User.objects.get(username=request.user.username)
    # user_profile = Profile.objects.get(user=user_object)

    # user_following_list = []
    # feed = []

    # user_following = FollowersCount.objects.filter(follower=request.user.username)

    # for users in user_following:
    #     user_following_list.append(users.user)

    # for usernames in user_following_list:
    #     feed_lists = Post.objects.filter(user=usernames)
    #     feed.append(feed_lists)

    # feed_list = list(chain(*feed))

    # # user suggestion starts
    # all_users = User.objects.all()
    # user_following_all = []

    # for user in user_following:
    #     user_list = User.objects.get(username=user.user)
    #     user_following_all.append(user_list)
    
    # new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    # current_user = User.objects.filter(username=request.user.username)
    # final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    # random.shuffle(final_suggestions_list)

    # username_profile = []
    # username_profile_list = []

    # for users in final_suggestions_list:
    #     username_profile.append(users.id)

    # for ids in username_profile:
    #     profile_lists = Profile.objects.filter(id_user=ids)
    #     username_profile_list.append(profile_lists)

    # suggestions_username_profile_list = list(chain(*username_profile_list))


    # return render(request, 'signin.html', {'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})

# def index(request):
#   if request.method=='POST':
#     username=request.POST.get('username')
#     password=request.POST.get('password')
#     if username and password:
#       user=authenticate(username=username,password=password)
#       print(username,password)
#       print(user)
#       if user is not None:
#         login(request,user)
#         return redirect('home')
#       else:
#         messages.error(request,'Username or Password is Incorrect')
#     else:
#       messages.error(request,'Fill out all the fields')
  
#   return render(request,'core/signin.html',{})


def loginUser(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.error(request, 'Credentials Invalid')
        return redirect('signin')

  else:
    return render(request, 'core/signin.html')
  # print("CCCCCCCCCCC1")
  # form=RegisterForm()
  # print(request.method)
  # if request.method=='POST':
  #   # print("CCCCCCCCCCCCCCC2")
  #   form=RegisterForm(request.POST)
  #   if form.is_valid():
  #     # print("CCCCCCCCCCCCCCCCCCCCCC3")
  #     form.save()
  #     # return redirect('signin')
  #     return render(request,'core/signin.html',{})
  # # else:
  # #   form=RegisterForm()
  # return render(request,'core/signup.html',{'form':form})


def registerUser(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username,email,password,password2)
    if password == password2:
      # print("CCCCCCCCC1")
      if User.objects.filter(email=email).exists():
        # print("CCCCCCCCC2")
        messages.error(request, 'Email Taken')
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        # print("CCCCCCCCC3")
        messages.error(request, 'Username Taken')
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        user_login = auth.authenticate(username=username, password=password)
        # print("QQQQQQQQQQQQQQQQQ")
        auth.login(request, user_login)
        print("FFFFF")
        user_model = User.objects.get(username=username)
        # print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        # print("OOOOOOOOOOOOOOO")
        return redirect('home')
    else:
      # print("SSSSSSSSSSSSSSSS")
      messages.error(request, 'Password Not Matching')
      return redirect('signup') 
  else:
    return render(request, 'core/signup.html')


  # # print("CCCCCCCCCCCCCCCCC1")
  # if request.method=='POST':
  #   # print("CCCCCCCCCCCCCCCCC2")
  #   username=request.POST.get('username')
  #   password=request.POST.get('password')
  #   # print("CCCCCCCCCCCCCCCCC3")
  #   # print(emailaddress,password)
  #   if username and password:
  #     user=authenticate(username=username,password=password)
  #     print(username,password)
  #     print(user)
  #     if user is not None:
  #       login(request,user)
  #       return redirect('home')
  #     else:
  #       messages.error(request,'Username or Password is Incorrect')
  #   else:
  #     messages.error(request,'Fill out all the fields')
  
  # return render(request,'core/signin.html',{})

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

def postjobs(request):
  return render(request,'core/postjobs.html',{})

@login_required(login_url='signin')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'core/profile.html', context)


