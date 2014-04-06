# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntryClassification'
        db.create_table(u'core_entryclassification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.EntryQueue'])),
            ('positive', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('negative', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('neutral', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'core', ['EntryClassification'])

        # Adding model 'ApiRequests'
        db.create_table(u'core_apirequests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('url', self.gf('django.db.models.fields.TextField')()),
            ('counter', self.gf('django.db.models.fields.IntegerField')()),
            ('until', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'core', ['ApiRequests'])


    def backwards(self, orm):
        # Deleting model 'EntryClassification'
        db.delete_table(u'core_entryclassification')

        # Deleting model 'ApiRequests'
        db.delete_table(u'core_apirequests')


    models = {
        u'core.apirequests': {
            'Meta': {'object_name': 'ApiRequests'},
            'counter': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'until': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.TextField', [], {})
        },
        u'core.area': {
            'Meta': {'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'rad': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
        },
        u'core.entryclassification': {
            'Meta': {'object_name': 'EntryClassification'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.EntryQueue']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'negative': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'neutral': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'positive': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'core.entryqueue': {
            'Meta': {'unique_together': "(('origin', 'origin_id'),)", 'object_name': 'EntryQueue'},
            'analysis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'areas': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Area']", 'symmetrical': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'author_id': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'origin_id': ('django.db.models.fields.BigIntegerField', [], {'blank': 'True'})
        },
        u'core.sourceforarea': {
            'Meta': {'object_name': 'SourceForArea'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Area']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'since_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']