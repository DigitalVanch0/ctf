from django.db import models


class Team(models.Model):
    name_team = models.CharField('название команды', max_length=20)
    rating = models.IntegerField('рейтинг команды')


class Uchastnik(models.Model):
    name_user = models.CharField('имя пользователя', max_length=20)
    surname_user = models.CharField('фамилия пользователя', max_length=20)
    nickname_user = models.CharField('никнейм пользователя', max_length=20)
    nameteam = models.CharField('название команды', max_length=20)
    role_user = models.CharField('роль пользователя', max_length=20)
    contact = models.CharField('контакт пользователя', max_length=20)
    information = models.TextField('информация о пользователе')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class Task(models.Model):
    task = models.FileField('задания')
    answer = models.CharField('ответ на задание', max_length=120)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(Uchastnik, on_delete=models.CASCADE)
