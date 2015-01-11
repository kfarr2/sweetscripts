# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('bio_id', models.AutoField(serialize=False, primary_key=True)),
                ('content', models.TextField()),
                ('is_public', models.BooleanField()),
            ],
            options={
                'db_table': 'bio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(serialize=False, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75)),
                ('birthday', models.DateField()),
            ],
            options={
                'db_table': 'contact',
            },
            bases=(models.Model,),
        ),
    ]
