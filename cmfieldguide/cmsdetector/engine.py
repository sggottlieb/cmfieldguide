import signatures
import pkgutil

def test(url):

    results = []
    for cms_name in get_cms_names():
        signature = __import__('cmfieldguide.cmsdetector.signatures.' + cms_name, 
            fromlist='Signature').Signature()
        
        results.append((signature.NAME, signature.run(url)))

    return results


def get_cms_names():

    results = []
    
    package = signatures
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        results.append(modname)

    return results

