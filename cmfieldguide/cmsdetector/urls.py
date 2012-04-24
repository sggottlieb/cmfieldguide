from django.conf.urls.defaults import patterns, include, url
from views import *


urlpatterns = patterns('',
    url(r'^reject/(?P<id>\d+)', platform_reject, name='platform_reject'),
    url(r'^$', index, name='detector_index'),
)
