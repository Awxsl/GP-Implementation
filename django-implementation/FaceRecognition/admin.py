# from django.contrib import admin

# from . import models

# @admin.register(models.User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'email_address', 'user_type']
#     list_editable = ['user_type']
#     ordering = ['first_name', 'last_name']
#     list_per_page = 20

# @admin.register(models.Course)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'course_code', 'name', 'credit_hours']
#     ordering = ['id']
#     list_per_page = 20

# @admin.register(models.Section)
# class SectionAdmin(admin.ModelAdmin):
#     list_display = ['id', 'course_id', 'instructor_id']
#     ordering = ['id']
#     list_per_page = 20

# @admin.register(models.Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username']
#     readonly_fields=('is_encoded',)
#     ordering = ['id']
#     list_per_page = 20


# @admin.register(models.Instructor)
# class InstructorAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username']
#     ordering = ['id']
#     list_per_page = 20
    
# @admin.register(models.RegisteredStudents)
# class RegisteredStudentsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'student_id', 'section_id']
#     ordering = ['id']
#     list_per_page = 20

# @admin.register(models.CrowdCount)
# class CrowdCountAdmin(admin.ModelAdmin):
#     list_display = ['id', 'instructor_id', 'attendees_count']
#     ordering = ['id']
#     list_per_page = 20

# @admin.register(models.Absence)
# class AbsenceAdmin(admin.ModelAdmin):
#     list_display = ['id', 'student_id', 'section_id', 'Date']
#     ordering = ['id']
#     list_per_page = 20

# @admin.register(models.ImageEncodings)
# class ImageEncodingAdmin(admin.ModelAdmin):
#     list_display = ['student', 'encoding']
#     ordering = ['student']
#     list_per_page = 20
    
from django.contrib import admin
from django.contrib.admin import forms
from . import models
from .models import User, Instructor

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email_address', 'user_type']
    list_editable = ['user_type']
    ordering = ['first_name', 'last_name']
    list_per_page = 20

    def save_model(self, request, obj, form, change):
        try: 
            return super().save_model(request, obj, form, change)
        except: 
            print('error')
        finally:
            if obj.user_type == 'I':
                instuctor = Instructor() 
                instuctor.username = User(pk=obj.pk)
                instuctor.save()




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
    readonly_fields=('is_encoded',)
    ordering = ['id']
    list_per_page = 20

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print('entered form field')
        if db_field.name == "username":
            kwargs['queryset'] = User.objects.filter(user_type='S')
        print(db_field.name)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']
    ordering = ['id']
    list_per_page = 20

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "username":
            kwargs['queryset'] = User.objects.filter(user_type='I')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


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

@admin.register(models.ImageEncodings)
class ImageEncodingAdmin(admin.ModelAdmin):
    list_display = ['student', 'encoding']
    ordering = ['student']
    list_per_page = 20
    
