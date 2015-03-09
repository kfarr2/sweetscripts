# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0002_auto_20150111_0654'),
    ]

    operations = [
        migrations.AddField(
            model_name='bio',
            name='avatar',
            field=models.ImageField(upload_to='', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=255, default='n/a'),
            preserve_default=False,
        ),
    ]
