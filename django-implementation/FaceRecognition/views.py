from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from FaceRecognition.models import *


# Create your views here.

#to check if already signed in or not in dashboards
username = ''

#Student or Instructor, to redirect to the appropriate page
type = ''

#to get the name for printing
name = ''


def test(request):
    return render(request, 'FaceRecognition/index.html', {'name': 'Omar'})

def index(request): 
    global username
    global type
    global name

    error = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #This chunk of try/except is only for preventing the server to throw an exception when
        #there is no such a user
        try:
            input_username = User.objects.get(username=username).username
            input_password = User.objects.get(username=username).password     
        except:
            return render(request, 'FaceRecognition/index.html', {'error': 'Enter a valid username/password', 'username': username})
        
        #Password has to be validated
        if password != input_password:
            return render(request, 'FaceRecognition/index.html', {'error': 'Enter a valid username/password', 'username': username})

        type = User.objects.get(username=username).user_type
        name = User.objects.get(username=username)
            
        if type == 'S':
            return redirect(student_dashboard)
        else:
            return redirect(instructor_dashboard)


    return render(request, 'FaceRecognition/index.html', {})

def student_dashboard(request):
    global username
    if username == '':
        return redirect(index)

    return render(request, 'FaceRecognition/student_dashboard.html', {'name': name})
    

def instructor_dashboard(request):
    global username
    if username == '':
        return redirect(index)
    
    return render(request, 'FaceRecognition/instructor_dashboard.html', {'name': name})


def choose_section(request):
    global username
    if username == '':
        return redirect(index)
    
    return render(request, 'FaceRecognition/choose_section.html')


def face_recognition(request):
    global username
    if username == '':
        return redirect(index)
    
    return render(request, 'FaceRecognition/face_recognition.html')


def crowd_counting(request):
    global username
    if username == '':
        return redirect(index)
    
    return render(request, 'FaceRecognition/crowd_counting.html')