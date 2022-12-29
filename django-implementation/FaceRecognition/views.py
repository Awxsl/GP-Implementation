from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from FaceRecognition.models import *
from FaceRecognition.serializers import ImageSerializer
from rest_framework.response import Response
import os, shutil, pickle, base64
import face_recognition
from PIL import Image, ImageDraw
import numpy as np


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


def absence_table(request):

    return render(request, 'FaceRecognition/absence_table.html')
    

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


def face_identification(request):
    global username
    if username == '':
        return redirect(index)

    DeleteImages()

    queryset = Student.objects.filter(is_encoded=False)
    for obj in queryset:
        face = face_recognition.load_image_file(obj.student_image)
        face_encoding = face_recognition.face_encodings(face)[0]
        encoding = ImageEncodings()
        encoding.student = Student(pk=obj.pk)
        binary = pickle.dumps(face_encoding)
        base64image = base64.b64encode(binary)
        encoding.encoding = base64image
        encoding.save()
        Student.objects.filter(pk=obj.pk).update(is_encoded=True)
        # student = Student(pk=obj.pk)
        # print(student.is_encoded)
        # # print(student)
        # student.is_encoded = True
        # student.save()


        

    return render(request, 'FaceRecognition/face_recognition.html')


def crowd_counting(request):
    global username
    if username == '':
        return redirect(index)
    
    np_bytes = base64.b64decode(ImageEncodings.objects.filter(pk=79)[0].encoding)
    np_array = pickle.loads(np_bytes)
    print(np_array)
    
    return render(request, 'FaceRecognition/crowd_counting.html')


def student_list(request):

    return render(request, 'FaceRecognition/student_list.html')


def results(request):
    attendees = []
    registered_faces = []
    names = []
    encodings = ImageEncodings.objects.all()
    
    for image in encodings:
        np_bytes = base64.b64decode(image.encoding)
        np_array = pickle.loads(np_bytes)
        registered_faces.append(np_array)
        names.append(image.student.username.first_name)


    attendees_image = face_recognition.load_image_file('FaceRecognition\\static\\images\\attendance.jpeg')
    face_locations = face_recognition.face_locations(attendees_image)
    face_encodings = face_recognition.face_encodings(attendees_image, face_locations)
    pil_image = Image.fromarray(attendees_image)
    draw = ImageDraw.Draw(pil_image)
    
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(registered_faces, face_encoding)
        name = "Unknown"

        face_distances = face_recognition.face_distance(registered_faces, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = names[best_match_index]
            


            


        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))

    for index, result in enumerate(matches): 
        if result == True:
            status = False
        else: 
            status = True

        abscence = Absence()
        student_id = ImageEncodings.objects.get(pk=index+1).student.pk
        abscence.student = Student(pk=student_id)
        abscence.section = Section(pk='1')
        abscence.is_absent = status
        abscence.save()
        print('created')

    del draw

    pil_image.save("FaceRecognition\\static\\images\\detected_faces.jpg")
    return render(request, 'FaceRecognition/submit_records.html')






# def store_image(request): 
#     if request.method == 'POST':
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
        

def DeleteImages():
    folder = 'FaceRecognition\static\images'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))