import email
from email.policy import default
from enum import unique
from random import choices
from tabnanny import verbose
from django.db import models

class User(models.Model):
    USER_TYPE = [
        ('I', 'Instructor'),
        ('S', 'Student')
    ]
    username = models.CharField(max_length=255, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=255)
    user_type = models.CharField(max_length=1, choices=USER_TYPE, default='S')

    class Meta:
        db_table = 'Users'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Instructor(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, verbose_name='User')

    class Meta:
        db_table = 'Instructors'
    
    def __str__(self):
        queryset = User.objects.get(username__exact=self.username_id)
        return queryset.first_name + ' ' + queryset.last_name

class Student(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, unique=True, verbose_name='User')
    student_image = models.ImageField(upload_to='images/', null=True)
    is_encoded = models.BooleanField(default=False)

    class Meta:
        db_table = 'Students'

    def __str__(self):
        queryset = User.objects.get(username__exact=self.username_id)
        return queryset.first_name + ' ' + queryset.last_name

class Course(models.Model):
    name = models.CharField(max_length=255)
    credit_hours = models.IntegerField()
    course_code = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'Courses'

    def __str__(self) -> str:
        return self.course_code + ' - ' + self.name

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT, verbose_name='Course', default='1')
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, verbose_name='Instructor', default='1')

    class Meta:
        db_table = 'Sections'

    def __str__(self) -> str:
        return 'Section ' + str(self.id)

class RegisteredStudents(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Section', default='1')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Student', default='1')

    class Meta:
        db_table = 'Registered_Students'

    def __str__(self) -> str:
        return f'{self.section_id} - {self.student_id}'

class Absence(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Section', default='1')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Student', default='1')
    is_absent = models.BooleanField(default=True)
    Date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Absence'

    def __str__(self) -> str:
        return f'Absence #{self.id}'
    
class CrowdCount(models.Model):
    attendees_count = models.IntegerField()
    Date = models.DateField(auto_now_add=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT, verbose_name='Instructor', default='1')

    class Meta:
        db_table = 'Crowd_Count'

    def __str__(self) -> str:
        return f'Count #{self.id}'


class ImageEncodings(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    encoding = models.BinaryField()


class AttendeesImage(models.Model):
    image = models.ImageField(upload_to='images/')
