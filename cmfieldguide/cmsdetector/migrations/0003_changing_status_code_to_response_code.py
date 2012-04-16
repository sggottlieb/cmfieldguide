# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Site.response_code'
        db.delete_column('cmsdetector_site', 'response_code')

        # Adding field 'Site.status_code'
        db.add_column('cmsdetector_site', 'status_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'Site.response_code'
        db.add_column('cmsdetector_site', 'response_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Site.status_code'
        db.delete_column('cmsdetector_site', 'status_code')

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
            'geturl': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'headers': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status_code': ('django.db.models.fields.IntegerField', [], {}),
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