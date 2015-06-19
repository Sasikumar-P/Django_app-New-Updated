# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sss', '0012_auto_20150618_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='grandmotherrname',
            new_name='grandmothername',
        ),
        migrations.RenameField(
            model_name='family',
            old_name='motherrname',
            new_name='mothername',
        ),
        migrations.AlterField(
            model_name='family',
            name='annualincome',
            field=models.IntegerField(),
        ),
    ]
