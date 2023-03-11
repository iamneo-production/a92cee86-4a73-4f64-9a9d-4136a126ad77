from django.urls import path
from . import views

appname='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.registerUser, name='signup'),
    path('signin/', views.loginUser, name='signin'),
    path('home/', views.home, name='home'),
    path('profiles/', views.profiles, name='profiles'),
    path('jobboards/', views.jobboards, name='jobboards'),
    path('eventlistings/', views.eventlistings, name='eventlistings'),
    path('joblistings/', views.joblisitings, name='joblistings'),
    path('connections/', views.connections, name='connections'),
]