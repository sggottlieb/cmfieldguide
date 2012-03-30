from django.conf.urls.defaults import patterns, include, url
from views import home
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^detect', include('cmsdetector.urls')),
    url(r'^$', home, name='home'),
    # url(r'^cmsid/', include('cmsid.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


