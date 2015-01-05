# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0009_auto_20150105_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/proj/personal/media'),
            preserve_default=True,
        ),
    ]
