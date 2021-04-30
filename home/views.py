from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,Profiles
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,request
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout

#for serial portS
from math import sin, cos, sqrt, atan2, radians
import serial



#from home.models import register

import json

# Create your views here.

def index(request):
    #return HttpResponse("this is home page")
    return render(request,"index.html")
    
def about(request): 
    return render(request,"about.html")

def service(request): 
    return render(request,"service.html")
@login_required(login_url='login')
def pass_val(request):
    data_from_post = json.load(request)['form'] #Get data from POST request
    #Do something with the data from the POST request
    #If sending data back to the view, create the data dictionary
    data = {
        'my_data':data_from_post,
        }
    data=data['my_data']
    print("lat is :", data['lat'])
    print("long is :", data['lng'])
    try:
        ser = serial.Serial('COM1', 9600)
        if ser.isOpen():
            print(ser.name + ' is open..')
    except :
        print("ERROR connecting to port")
        input()
        exit()
    #print("Should be:", 278.546, "km")

    class location:
        def __init__(self,lat,lon):
            self.lat = lat
            self.lon = lon

    #location location3
    def calculator(x,y):
        R=6367.0
        x.lat=radians(x.lat)
        x.lon=radians(x.lon)
        y.lat=radians(y.lat)
        y.lon=radians(y.lon)

        dlon = float(y.lon)- float(x.lon)
        dlat = float(y.lat) - float(x.lat)

        a = sin(dlat / 2)**2 + cos(x.lat) * cos(y.lat) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance

    location1=location(52.2296756,21.0122287)
    #location2=location(52.406374,16.9251681)
    location3=location(data['lat'],data['lng'])
    dist=calculator(location3,location1)
    #dis1=calculator(location3,location2)
    print(dist,"km")
    var=1

    if dist>1:
        var+=1
        print(var)
        try:
                ser.write(b'1')
                print("Sending data")
        except:
                print("Error on sending data")
        dist=calculator(location3,location1)
    
    
    return JsonResponse(data)


def contact(request): 
    print("Rajah  123")
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        contact= Contact(name=name, email=email, phone=number, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'your form has been sent !')
    return render(request,"contact.html")

def loginpage(request): 
    if request.method == "POST":
        username = request.POST.get('usernameName')
        password = request.POST.get('loginPassword')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"username or password incorrect")
    return render(request,"login.html")

def logoutuser(request):
    auth.logout(request)
    return redirect("/")

def register(request): 
    print("hello")
    if request.method == "POST":
        first_name = request.POST.get('fName')
        last_name= request.POST.get('lName')
        username=request.POST.get('username')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password1=request.POST.get('Password1')
        password2=request.POST.get('Password2')
        vehicle=request.POST.get('vehicle')
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                new_profile=Profiles(user=user,vehicle=vehicle,phone=number)
                new_profile.save()
                
                messages.success(request, 'your registration  has been sent !')
                return redirect("/")
        else:
            messages.info(request,"Password didnt matched")
            return redirect("register")

    else:
        return render(request,"register.html")
@login_required(login_url='login')
def map(request): 
    return render(request,"geolocation.html")

@login_required(login_url='login')
def home1(request):
    return render(request,"home1.html")
