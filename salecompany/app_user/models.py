from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Должность – одно значение из таблицы должностей.
class DolznostCustomUser(models.Model):
    name = models.CharField('Должность', max_length=255, null=True)
    title = models.CharField('Описание должности', max_length=255, null=True)

    def __str__(self):
        return self.name 

# кроме того, пользователь должен иметь одну из трех ролей: Администратор, Супервайзер, Пользователь.
class RoleCustomUser(models.Model):
    class Roles(models.IntegerChoices):
        ADMIN = 1, 'Администратор'
        SUPERVISOR = 2, 'Супервайзер'
        USER = 3, 'Пользователь'

    codename = models.CharField(max_length=255, choices=Roles.choices, default=Roles.USER)
    title = models.CharField('Описание роли', max_length=255, null=True)

    def __str__(self):
        return self.codename
        
# Каждый пользователь, независимо от роли, может поменять свое фото
class PhotoCustomUser(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# Модель пользователя
class CustomUser(AbstractUser):
    # Email – уникальное значение
    email = models.EmailField(('email'), unique=True)
    first_name = models.CharField('Имя', max_length=50, null=True)
    second_name = models.CharField('Фамилия', max_length=50, null=True)
    birth_day = models.DateField('Дата рождения', null=True)
    photo = models.ForeignKey(PhotoCustomUser, verbose_name='Фото', on_delete=models.SET_NULL, null=True) 
    dolznost = models.ForeignKey(DolznostCustomUser, verbose_name='Должность', on_delete=models.SET_NULL, null=True)
    role = models.ForeignKey(RoleCustomUser, on_delete=models.SET_NULL, null=True)
    # Каждый Пользователь имеет ровно одного начальника среди Супервайзеров.
    head = models.ForeignKey('CustomUser', related_name='subs', null=True, on_delete=models.SET_NULL)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def __str__(self):
        return self.email