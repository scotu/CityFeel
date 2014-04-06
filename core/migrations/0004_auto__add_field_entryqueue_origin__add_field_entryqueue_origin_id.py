# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EntryQueue.origin'
        db.add_column(u'core_entryqueue', 'origin',
                      self.gf('django.db.models.fields.CharField')(default='twitter', max_length=200),
                      keep_default=False)

        # Adding field 'EntryQueue.origin_id'
        db.add_column(u'core_entryqueue', 'origin_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'EntryQueue.origin'
        db.delete_column(u'core_entryqueue', 'origin')

        # Deleting field 'EntryQueue.origin_id'
        db.delete_column(u'core_entryqueue', 'origin_id')


    models = {
        u'core.area': {
            'Meta': {'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.entryqueue': {
            'Meta': {'object_name': 'EntryQueue'},
            'analysis': ('django.db.models.fields.BooleanField', [], {}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Area']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']