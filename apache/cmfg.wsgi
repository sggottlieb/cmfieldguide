import os, sys
sys.path.append('/home/ubuntu/cmfg')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cmfieldguide.settings'
import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    os.environ['RF_DBUSER'] = environ['RF_DBUSER']
    os.environ['RF_DBPASS'] = environ['RF_DBPASS']
    os.environ['RF_DBHOST'] = environ['RF_DBHOST']
    os.environ['RF_DBNAME'] = environ['RF_DBNAME']
    return _application(environ, start_response)