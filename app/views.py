import re
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from app.models import Masks, Profile, City, Symptoms, Vaccines
from decimal import *

# Homepage and Authentication
def home_v(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user = request.user)
        cert = current_user.certificate
        return render(request, 'home.html',{'cert':cert})
    else:
        return render(request, 'home.html')

def logout_v(request):
    logout(request)
    return redirect('home')

def register_v(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['e-mail']
            password = request.POST['password']
            password_repeat = request.POST['password_repeat']

            if username and email and password and password_repeat:
                if password != password_repeat:
                    messages.error(request,("Passwords do not match. Try Again"))
                    return redirect('register')

                try:
                    user = User.objects.get(username=username)
                    messages.error(request,("Username is already taken. Try Again"))
                    return redirect('register')
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username,email=email,password=password)
                    profile = Profile(user = user)
                    profile.save()

                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request,("Please enter all the fields."))
                return redirect('register')
        else:
            return render(request, 'register.html')

def login_v(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ("Username or Password was not found. Try Again or Register"))
            return redirect('login')
    else:
        return redirect('home')

#Webpages

def covid_info_v(request):
    if request.user.is_authenticated:
        return render(request, 'covid_info.html')
    else:
        return redirect('home')

def covid_quiz_v(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            points = 0
            q1 = request.POST['q1']
            q2 = request.POST['q2']
            q3 = request.POST['q3']
            q4 = request.POST['q4']
            q5 = request.POST['q5']

            if (q1 == '1'):
                points += 1
            if (q2 == '3'):
                points += 1
            if (q3 == '1'):
                points += 1
            if (q4 == '3'):
                points += 1
            if (q5 == '4'):
                points += 1

            print(q1, q2 ,q3 ,q4 ,q5)
            print(points)
            if (points == 5):
                current_user = Profile.objects.get(user = request.user)
                current_user.certificate = 'True'
                current_user.save()
                
            return render(request, 'covid_quiz.html',{'points':points})
        else:
            hide = False
            return render(request, 'covid_quiz.html',{'hide':hide})
    else:
        return redirect('home')

def map_v(request):
    if request.user.is_authenticated:
        cities = City.objects.all()
        return render(request, 'map.html', {'cities':cities})
    else:
        return redirect('home')

def info_v(request, name):
    if request.user.is_authenticated:
        if name == 'symptoms':
            symptoms = Symptoms.objects.all() 
            return render(request,name+'.html', {'symptoms':symptoms})
        elif name == 'vaccines':
            vaccines = Vaccines.objects.all() 
            return render(request,name+'.html', {'vaccines':vaccines})
        elif name == 'masks':
            masks = Masks.objects.all()
            return render(request,name+'.html', {'masks':masks})
        elif name == 'general_info':
            return render(request,name+'.html')
    else:
        return redirect('home')