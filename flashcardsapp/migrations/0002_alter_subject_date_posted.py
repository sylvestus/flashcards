# Generated by Django 4.0.4 on 2022-04-20 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
