# Generated by Django 4.2 on 2023-05-25 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_mails_delete_mail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mails',
            name='date',
        ),
        migrations.AddField(
            model_name='mails',
            name='maildate',
            field=models.DateField(auto_now=True),
        ),
    ]
