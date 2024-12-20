# Generated by Django 5.1.1 on 2024-09-29 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyProgram', '0003_problem_programing_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Ник')),
                ('description', models.TextField(verbose_name='Имя Фамилия')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('2', 'WAIT'), ('1', 'OK'), ('0', 'FAIL')], default='2', max_length=1)),
                ('code', models.TextField()),
                ('problem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studyProgram.problem')),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studyProgram.student')),
            ],
        ),
    ]
