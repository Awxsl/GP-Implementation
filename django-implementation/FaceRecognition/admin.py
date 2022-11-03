from django.contrib import admin

from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address', 'user_type']
    list_editable = ['user_type']
    ordering = ['first_name', 'last_name']
    list_per_page = 20

@admin.register(models.Course)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_code', 'name', 'credit_hours']
    ordering = ['id']
    list_per_page = 20

@admin.register(models.Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'course_id', 'instructor_id']
    ordering = ['id']
    list_per_page = 20

@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    ordering = ['id']
    list_per_page = 20

@admin.register(models.Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    ordering = ['id']
    list_per_page = 20
    
@admin.register(models.RegisteredStudents)
class RegisteredStudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'section_id']
    ordering = ['id']
    list_per_page = 20

@admin.register(models.CrowdCount)
class CrowdCountAdmin(admin.ModelAdmin):
    list_display = ['id', 'instructor_id', 'attendees_count']
    ordering = ['id']
    list_per_page = 20

@admin.register(models.Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_id', 'section_id', 'Date']
    ordering = ['id']
    list_per_page = 20
