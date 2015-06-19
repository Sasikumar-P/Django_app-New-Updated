# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0010_auto_20150618_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fathername', models.CharField(max_length=30)),
                ('motherrname', models.CharField(max_length=30)),
                ('brothername', models.CharField(max_length=30)),
                ('sistername', models.CharField(max_length=30)),
                ('grandfathername', models.CharField(max_length=30)),
                ('grandmotherrname', models.CharField(max_length=30)),
                ('annualincome', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='page',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
