from django.db import models
from django.contrib.auth.models import User


class UserTable(models.Model):
    name = models.CharField('Имя', max_length=50)
    second_name = models.CharField('Фамилия', max_length=50)
    profile_image = models.ImageField(upload_to='./static/for_users/img/',
                                      default='/static/for_users/img/cat_profile.jpg')
    email = models.CharField('Почта', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
