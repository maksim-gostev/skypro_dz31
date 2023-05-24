from django.db import models
from django.contrib.auth.models import AbstractUser



class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'локация'
        verbose_name_plural = 'локации'


class User(AbstractUser):
    ROLE = [
        ('admin', 'Администратор'),
        ('moderator', 'Модератор'),
        ('member', 'Пользователь')
    ]



    role = models.CharField(max_length=20, choices=ROLE, default="member")
    age = models.PositiveIntegerField()
    location = models.ManyToManyField(Location, null=True)
    birth_date = models.DateField(null=True)
    email = models.CharField(max_length=100, null=True, unique=True)


    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
