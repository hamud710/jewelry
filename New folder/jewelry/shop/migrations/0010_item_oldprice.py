# Generated by Django 3.2.9 on 2021-12-01 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_compare'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='oldPrice',
            field=models.FloatField(default=0.0),
        ),
    ]
