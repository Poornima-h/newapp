# Generated by Django 3.2.5 on 2021-08-06 04:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0030_auto_20210805_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 4, 28, 30, 453490, tzinfo=utc)),
        ),
    ]
