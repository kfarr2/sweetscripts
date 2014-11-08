# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Admin'
        db.create_table('admin', (
            ('admin_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255, unique=True)),
        ))
        db.send_create_signal('home', ['Admin'])


    def backwards(self, orm):
        # Deleting model 'Admin'
        db.delete_table('admin')


    models = {
        'home.admin': {
            'Meta': {'object_name': 'Admin', 'db_table': "'admin'"},
            'admin_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True'})
        }
    }

    complete_apps = ['home']