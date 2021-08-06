# Generated by Django 3.2.5 on 2021-08-05 07:25

import app1.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_auto_20210805_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='comment',
            field=models.CharField(blank=True, default='comment#', max_length=200, null=True, validators=[app1.models.validate_comment]),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 5, 7, 25, 56, 180286, tzinfo=utc)),
        ),
    ]
