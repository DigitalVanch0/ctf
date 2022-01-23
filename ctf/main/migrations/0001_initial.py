# Generated by Django 3.2.9 on 2022-01-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authentification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=400, verbose_name='логин')),
                ('password', models.CharField(max_length=400, verbose_name='пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=20, verbose_name='название команды')),
                ('rating', models.IntegerField(verbose_name='рейтинг команды')),
            ],
        ),
        migrations.CreateModel(
            name='Uchastnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=20, verbose_name='имя пользователя')),
                ('surname_user', models.CharField(max_length=20, verbose_name='фамилия пользователя')),
                ('nickname_user', models.CharField(max_length=20, verbose_name='никнейм пользователя')),
                ('nameteam', models.CharField(max_length=20, verbose_name='название команды')),
                ('role_user', models.CharField(max_length=20, verbose_name='роль пользователя')),
                ('contact', models.CharField(max_length=20, verbose_name='контакт пользователя')),
                ('information', models.TextField(verbose_name='информация о пользователе')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.FileField(upload_to='', verbose_name='задания')),
                ('answer', models.CharField(max_length=120, verbose_name='ответ на задание')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.uchastnik')),
            ],
        ),
    ]
