# Generated by Django 3.2.13 on 2023-05-10 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_customuser_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
    ]
