# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'EntryQueue.author_id'
        db.add_column(u'core_entryqueue', 'author_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'EntryQueue', fields ['origin', 'origin_id']
        db.create_unique(u'core_entryqueue', ['origin', 'origin_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EntryQueue', fields ['origin', 'origin_id']
        db.delete_unique(u'core_entryqueue', ['origin', 'origin_id'])

        # Deleting field 'EntryQueue.author_id'
        db.delete_column(u'core_entryqueue', 'author_id')


    models = {
        u'core.area': {
            'Meta': {'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'core.entryqueue': {
            'Meta': {'unique_together': "(('origin', 'origin_id'),)", 'object_name': 'EntryQueue'},
            'analysis': ('django.db.models.fields.BooleanField', [], {}),
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Area']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'origin_id': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'original': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['core']