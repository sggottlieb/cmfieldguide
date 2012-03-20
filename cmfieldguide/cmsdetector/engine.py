import signatures
import pkgutil
from operator import itemgetter, attrgetter

from cmfieldguide.cmsdetector.signatures import PageCache

def test(url):
    
    page_cache = PageCache()
    
    platforms = []
    for platform_name in get_platform_names():
        platforms.append(__import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
            fromlist='Signature').Signature(url, page_cache))
    
    return sorted(platforms, key=attrgetter('confidence'), reverse=True)


def get_platform_names():

    names = []
    
    package = signatures
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        names.append(modname)

    return names

