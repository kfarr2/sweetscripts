# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stuff', '0007_auto_20150103_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('post', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'blog',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='project',
            name='screenshot',
            field=models.ImageField(upload_to='/home/proj/personal/media'),
            preserve_default=True,
        ),
        migrations.AlterModelTable(
            name='projectfile',
            table='project_file',
        ),
    ]
