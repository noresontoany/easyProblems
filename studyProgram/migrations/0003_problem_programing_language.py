# Generated by Django 5.1.1 on 2024-09-29 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyProgram', '0002_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='programing_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studyProgram.programinglanguage'),
        ),
    ]
