# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(default='none', upload_to='/media/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='site_url',
            field=models.URLField(default='none'),
            preserve_default=False,
        ),
    ]
