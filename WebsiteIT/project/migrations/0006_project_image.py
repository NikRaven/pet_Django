# Generated by Django 5.0 on 2023-12-27 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/img/1.jpg', upload_to='static/img'),
        ),
    ]