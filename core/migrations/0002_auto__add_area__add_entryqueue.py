# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table(u'core_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'core', ['Area'])

        # Adding model 'EntryQueue'
        db.create_table(u'core_entryqueue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Area'])),
            ('original', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['EntryQueue'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table(u'core_area')

        # Deleting model 'EntryQueue'
        db.delete_table(u'core_entryqueue')


    models = {
        u'core.area': {
            'Meta': {'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.entryqueue': {
            'Meta': {'object_name': 'EntryQueue'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Area']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']