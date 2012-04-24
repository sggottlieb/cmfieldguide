from django.contrib import admin
from models import *

class PlatformAdmin(admin.ModelAdmin):
    model = PlatformSiteTest
    search_fields = ['site__url', 'platform_name']
    list_filter = ['platform_name', 'visitor_rejects']

admin.site.register(Site)
admin.site.register(PlatformSiteTest, PlatformAdmin)
admin.site.register(TestResult)  