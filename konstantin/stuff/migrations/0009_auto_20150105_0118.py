# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0008_auto_20150104_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/konstantin/workspace/personal/media'),
            preserve_default=True,
        ),
    ]
