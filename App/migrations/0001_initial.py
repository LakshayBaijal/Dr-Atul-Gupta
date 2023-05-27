# Generated by Django 4.2 on 2023-05-25 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=15)),
                ('mobile', models.CharField(blank=True, max_length=15)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
