# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PlatformSiteTest.platform'
        db.delete_column('cmsdetector_platformsitetest', 'platform')

        # Adding field 'PlatformSiteTest.platform_name'
        db.add_column('cmsdetector_platformsitetest', 'platform_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'PlatformSiteTest.platform_website'
        db.add_column('cmsdetector_platformsitetest', 'platform_website',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'PlatformSiteTest.explanation'
        db.add_column('cmsdetector_platformsitetest', 'explanation',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

    def backwards(self, orm):
        # Adding field 'PlatformSiteTest.platform'
        db.add_column('cmsdetector_platformsitetest', 'platform',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Deleting field 'PlatformSiteTest.platform_name'
        db.delete_column('cmsdetector_platformsitetest', 'platform_name')

        # Deleting field 'PlatformSiteTest.platform_website'
        db.delete_column('cmsdetector_platformsitetest', 'platform_website')

        # Deleting field 'PlatformSiteTest.explanation'
        db.delete_column('cmsdetector_platformsitetest', 'explanation')

    models = {
        'cmsdetector.platformsitetest': {
            'Meta': {'object_name': 'PlatformSiteTest'},
            'confidence': ('django.db.models.fields.IntegerField', [], {}),
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'platform_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'platform_website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
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