# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='is_public',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
