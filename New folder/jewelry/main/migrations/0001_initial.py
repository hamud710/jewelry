# Generated by Django 3.2.9 on 2021-11-29 17:05

from django.db import migrations, models
import djrichtextfield.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Quotes', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('AboutUs', djrichtextfield.models.RichTextField()),
                ('WhatDoWeDo', djrichtextfield.models.RichTextField()),
                ('OurMission', djrichtextfield.models.RichTextField()),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=13)),
                ('image', models.ImageField(upload_to='MyImage/')),
            ],
        ),
    ]
