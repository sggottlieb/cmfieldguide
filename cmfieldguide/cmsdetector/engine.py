import signatures
import pkgutil
import datetime
from operator import itemgetter, attrgetter

from cmfieldguide.cmsdetector.models import Site, Page, save_as_site_object


def test(url, force_new=False):
    
    #Looking for the site in the database
    site_cache = Site.objects.filter(url=url)
    site_cache = site_cache.filter(date_time__gt=datetime.datetime.now()-datetime.timedelta(days=1))
    
    #if force_new:
    if force_new:
     site_cache = site_cache.delete()
    
    #If we found it, use it.
    if site_cache:
        site = site_cache[0]
    else:
        site = save_as_site_object(Page(url))
    
        for platform_name in get_platform_names():
            signature = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                fromlist='Signature').Signature(site)
    
    return site


def get_platform_names():

    names = []
    
    package = signatures
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        names.append(modname)

    return names

