from django.urls import path
from . import views 

urlpatterns = [
    path('test/', views.test),
    path('', views.index),
    path('student_dashboard/', views.student_dashboard),
    path('instructor_dashboard/', views.instructor_dashboard),
    path('choose_section/', views.choose_section),
    path('face_identification/', views.face_identification),
    path('crowd_counting/', views.crowd_counting),
    path('absence_table/', views.absence_table),
    path('student_list/', views.student_list),
    path('results/', views.results),
]