# Generated by Django 3.2.5 on 2021-08-06 07:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0035_auto_20210806_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 7, 48, 32, 336959, tzinfo=utc)),
        ),
    ]
