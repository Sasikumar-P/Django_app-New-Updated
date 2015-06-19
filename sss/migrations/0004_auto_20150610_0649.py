# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0003_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='author',
            name='city',
            field=models.CharField(default=0, max_length=60),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='author',
            name='phonenumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='author',
            name='state',
            field=models.CharField(default=0, max_length=30),
        ),
    ]
