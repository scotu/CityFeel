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
            ('lat', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('long', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('rad', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
        ))
        db.send_create_signal(u'core', ['Area'])

        # Adding model 'SourceForArea'
        db.create_table(u'core_sourceforarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Area'])),
            ('since_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('max_id', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['SourceForArea'])

        # Adding model 'EntryQueue'
        db.create_table(u'core_entryqueue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('origin_id', self.gf('django.db.models.fields.BigIntegerField')(blank=True)),
            ('message', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('author_id', self.gf('django.db.models.fields.BigIntegerField')(blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('analysis', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('lat', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('long', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['EntryQueue'])

        # Adding M2M table for field areas on 'EntryQueue'
        m2m_table_name = db.shorten_name(u'core_entryqueue_areas')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entryqueue', models.ForeignKey(orm[u'core.entryqueue'], null=False)),
            ('area', models.ForeignKey(orm[u'core.area'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entryqueue_id', 'area_id'])

        # Adding unique constraint on 'EntryQueue', fields ['origin', 'origin_id']
        db.create_unique(u'core_entryqueue', ['origin', 'origin_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EntryQueue', fields ['origin', 'origin_id']
        db.delete_unique(u'core_entryqueue', ['origin', 'origin_id'])

        # Deleting model 'Area'
        db.delete_table(u'core_area')

        # Deleting model 'SourceForArea'
        db.delete_table(u'core_sourceforarea')

        # Deleting model 'EntryQueue'
        db.delete_table(u'core_entryqueue')

        # Removing M2M table for field areas on 'EntryQueue'
        db.delete_table(db.shorten_name(u'core_entryqueue_areas'))


    models = {
        u'core.area': {
            'Meta': {'object_name': 'Area'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'long': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'rad': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'})
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