# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0003_auto_20141116_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/konstantin/workspace/personal/media'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='site_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
    ]
