# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0006_auto_20150103_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_completed',
            field=models.DateTimeField(blank=True),
            preserve_default=True,
        ),
    ]
