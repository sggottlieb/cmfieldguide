from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    # url(r'^cmsid/', include('cmsid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT} ),
    )
