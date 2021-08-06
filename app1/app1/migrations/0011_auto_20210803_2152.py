# Generated by Django 3.2.5 on 2021-08-04 04:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_book_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='profile',
            field=models.ImageField(null=True, upload_to='media/images/'),
        ),
        migrations.AddField(
            model_name='book',
            name='resume',
            field=models.FileField(null=True, upload_to='media/userfiles/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 4, 4, 52, 48, 960884, tzinfo=utc)),
        ),
    ]