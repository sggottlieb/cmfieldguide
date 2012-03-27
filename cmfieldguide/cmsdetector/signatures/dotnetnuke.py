"""
This signature containts test to see if the site is running on DotNetNuke.
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
    
    NAME = 'DotNetNuke'
    WEBSITE = 'http://www.dotnetnuke.com/'
    KNOWN_POSITIVE = 'http://www.dotnetnuke.com/'
    TECHNOLOGY = '.NET'

    def test_has_portals_default(self, url):
        """
        DotNetNuke likes to store CSS and other resources in a Portals/_default folder.
        """
        
        if self.page_cache[get_url_stem(url)].contains_pattern('="/Portals/_default'):
            return 1
        else:
            return 0
        
