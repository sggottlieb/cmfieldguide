"""
This signature containts test to see if the site is running on EPiServer.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature, get_url_stem

class Signature(BaseSignature):

    NAME = 'Ektron'
    WEBSITE = 'http://www.ektron.com'
    KNOWN_POSITIVE = 'http://www.ektron.com'
    TECHNOLOGY = '.NET'

    def test_has_workarea_directory(self, url):
        """
        Ektron likes to store style sheets and javascripts in a rood directory called
        'Workarea'
        """
        
        if self.page_cache[url].contains_pattern('="/workarea', ignorecase=True):
            return 1
        else:
            return 0
            
    