import os, sys
sys.path.append('/home/ubuntu/cmfg')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cmfieldguide.settings'
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['CMFG_DBPASS'] = environ['CMFG_DBPASS']
    os.environ['CMFG_SECRET_KEY'] = environ['CMFG_SECRET_KEY']
    os.environ['CMFG_EMAIL_PASSWORD'] = environ['CMFG_EMAIL_PASSWORD']
        
    return _application(environ, start_response)