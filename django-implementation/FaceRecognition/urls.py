from django.urls import path
from . import views 

urlpatterns = [
    path('test/', views.test),
    path('', views.index),
    path('student_dashboard/', views.student_dashboard),
    path('instructor_dashboard/', views.instructor_dashboard),
    path('choose_section/', views.choose_section),
    path('face_recognition/', views.face_recognition),
    path('crowd_counting/', views.crowd_counting),
]