# Generated by Django 3.0.6 on 2020-07-22 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200711_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='course_time',
            field=models.TimeField(default=False),
        ),
    ]
