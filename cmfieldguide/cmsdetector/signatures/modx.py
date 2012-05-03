"""
This signature containts test to see if the site is running on ModX.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'Modx'
    WEBSITE = 'http://modx.com/'
    KNOWN_POSITIVE = 'http://modx.com/'
    TECHNOLOGY = 'PHP'

    def test_has_css_version_querystring(self, site):
        """
        Modx compresses and versions its style sheets.  It takes a querystring parameter to determine what version.
        """
        
        if site.home_page.has_matching_tag('link', {'rel':'stylesheet','href':'\.css\?v=[0-9]'}):
            return 1
        else:
            return 0
            
            
        
