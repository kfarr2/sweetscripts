# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0002_auto_20141115_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/personal/konstantin/media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
