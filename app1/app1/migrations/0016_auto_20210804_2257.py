# Generated by Django 3.2.5 on 2021-08-05 05:57

import app1.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 5, 57, 55, 895212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(max_length=100, validators=[app1.models.validate_dehli]),
        ),
    ]
