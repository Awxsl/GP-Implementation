# Generated by Django 4.1.2 on 2022-12-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FaceRecognition', '0010_remove_imageencodings_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageencodings',
            name='encoding',
            field=models.BinaryField(),
        ),
    ]