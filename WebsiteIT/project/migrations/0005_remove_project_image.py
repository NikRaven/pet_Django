# Generated by Django 5.0 on 2023-12-27 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
    ]
