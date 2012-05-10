# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for tst in orm['cmsdetector.PlatformSiteTest'].objects.filter(explanation__startswith='This site cannot be'):
            if tst.confidence == 0:
                tst.confidence = -1
                tst.save()
        


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'cmsdetector.platformsitetest': {
            'Meta': {'ordering': "['-site__date_time', 'platform_name']", 'object_name': 'PlatformSiteTest'},
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'cmsdetector.testresult': {
            'Meta': {'object_name': 'TestResult'},
            'explanation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'result': ('django.db.models.fields.IntegerField', [], {}),
            'test_run': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsdetector.PlatformSiteTest']"})
        }
    }

    complete_apps = ['cmsdetector']
    symmetrical = True
