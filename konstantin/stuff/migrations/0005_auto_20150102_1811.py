# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0004_auto_20141219_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('bio_id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'bio',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/proj/personal/media'),
            preserve_default=True,
        ),
    ]
