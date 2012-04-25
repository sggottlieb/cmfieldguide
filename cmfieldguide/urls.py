from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from views import detector_forward

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^detect/', include('cmfieldguide.cmsdetector.urls')),
    url(r'^$', detector_forward, name='detector_forward'),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ),
    )

