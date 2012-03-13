import signatures
import pkgutil

def test(url):

    results = Results()

    for signature in get_signatures():
        this_signature = __import__('cmfieldguide.signatures.' + signature, fromlist='run')
        results.add_platform(this_signature.name, this_signature.run())

    return results


def get_signatures():

    results = []

    package = signatures
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        results.append(modname)

    return results

class Results():

    platforms = {}

    def add_platform(self, name, results):
        self.platforms[name] = results
