# Generated by Django 2.0.3 on 2018-03-16 12:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gist',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 16, 17, 43, 11, 466872)),
        ),
    ]
