# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table('cmsdetector_site', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('response_code', self.gf('django.db.models.fields.IntegerField')()),
            ('date_time', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('cmsdetector', ['Site'])

        # Adding model 'PlatformSiteTest'
        db.create_table('cmsdetector_platformsitetest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsdetector.Site'])),
            ('platform', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')()),
            ('visitor_rejects', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cmsdetector', ['PlatformSiteTest'])

        # Adding model 'TestResult'
        db.create_table('cmsdetector_testresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test_run', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsdetector.PlatformSiteTest'])),
            ('result', self.gf('django.db.models.fields.IntegerField')()),
            ('explanation', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('cmsdetector', ['TestResult'])

    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table('cmsdetector_site')

        # Deleting model 'PlatformSiteTest'
        db.delete_table('cmsdetector_platformsitetest')

        # Deleting model 'TestResult'
        db.delete_table('cmsdetector_testresult')

    models = {
        'cmsdetector.platformsitetest': {
            'Meta': {'object_name': 'PlatformSiteTest'},
            'confidence': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsdetector.Site']"}),
            'visitor_rejects': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'cmsdetector.site': {
            'Meta': {'object_name': 'Site'},
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'response_code': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cmsdetector.testresult': {
            'Meta': {'object_name': 'TestResult'},
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('django.db.models.fields.IntegerField', [], {}),
            'test_run': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsdetector.PlatformSiteTest']"})
        }
    }

    complete_apps = ['cmsdetector']