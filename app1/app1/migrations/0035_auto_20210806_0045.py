# Generated by Django 3.2.5 on 2021-08-06 07:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0034_alter_book_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('author_language', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_a', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 6, 7, 45, 39, 694478, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.BigIntegerField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app1.employee')),
            ],
        ),
        migrations.CreateModel(
            name='novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novel_name', models.CharField(max_length=200)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.author')),
            ],
        ),
        migrations.CreateModel(
            name='club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=200)),
                ('member', models.ManyToManyField(to='app1.member')),
            ],
        ),
    ]