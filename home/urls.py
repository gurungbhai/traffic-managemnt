from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("service", views.service,name='service'),
    path("contact", views.contact,name='contact'),
    path("login", views.loginpage,name='login'),
     path("logout", views.logoutuser,name='logout'),
    path("register", views.register,name='register'),
    path("map", views.map,name='map'),
    path("home1", views.home1,name='home1'),
    path("pass_val", views.pass_val,name='data')


    
]
