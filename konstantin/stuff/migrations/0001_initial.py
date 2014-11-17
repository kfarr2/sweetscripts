# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('files', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_completed', models.DateTimeField()),
                ('team', models.TextField()),
            ],
            options={
                'db_table': 'project',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('project_file_id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='files.File', null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='stuff.Project', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
