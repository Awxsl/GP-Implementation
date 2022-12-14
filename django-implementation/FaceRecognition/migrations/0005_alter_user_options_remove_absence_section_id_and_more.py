# Generated by Django 4.1.2 on 2022-10-30 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0004_course_course_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.RemoveField(
            model_name='absence',
            name='section_id',
        ),
        migrations.RemoveField(
            model_name='absence',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='crowdcount',
            name='instructor_id',
        ),
        migrations.RemoveField(
            model_name='registeredstudents',
            name='section_id',
        ),
        migrations.RemoveField(
            model_name='registeredstudents',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='section',
            name='course_id',
        ),
        migrations.RemoveField(
            model_name='section',
            name='instructor_id',
        ),
        migrations.AddField(
            model_name='absence',
            name='section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.section', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='absence',
            name='student',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.student', verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='crowdcount',
            name='instructor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='FaceRecognition.instructor', verbose_name='Instructor'),
        ),
        migrations.AddField(
            model_name='registeredstudents',
            name='section',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.section', verbose_name='Section'),
        ),
        migrations.AddField(
            model_name='registeredstudents',
            name='student',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.student', verbose_name='Student'),
        ),
        migrations.AddField(
            model_name='section',
            name='course',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='FaceRecognition.course', verbose_name='Course'),
        ),
        migrations.AddField(
            model_name='section',
            name='instructor',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='FaceRecognition.instructor', verbose_name='Instructor'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.user', unique=True, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FaceRecognition.user', unique=True, verbose_name='User'),
        ),
    ]
