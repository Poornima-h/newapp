# Generated by Django 3.2.5 on 2021-08-05 06:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_auto_20210804_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 6, 28, 46, 768581, tzinfo=utc)),
        ),
    ]
