# Generated by Django 4.1.2 on 2022-12-27 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0009_student_is_encoded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageencodings',
            name='section',
        ),
    ]
