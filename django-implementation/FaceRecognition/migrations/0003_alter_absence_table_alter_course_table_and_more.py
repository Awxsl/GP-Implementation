# Generated by Django 4.1.2 on 2022-10-29 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0002_student_registeredstudents_instructor_crowdcount_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='absence',
            table='Absence',
        ),
        migrations.AlterModelTable(
            name='course',
            table='Courses',
        ),
        migrations.AlterModelTable(
            name='crowdcount',
            table='Crowd_Count',
        ),
        migrations.AlterModelTable(
            name='instructor',
            table='Instructors',
        ),
        migrations.AlterModelTable(
            name='registeredstudents',
            table='Registered_Students',
        ),
        migrations.AlterModelTable(
            name='section',
            table='Sections',
        ),
        migrations.AlterModelTable(
            name='student',
            table='Students',
        ),
        migrations.AlterModelTable(
            name='user',
            table='Users',
        ),
    ]
