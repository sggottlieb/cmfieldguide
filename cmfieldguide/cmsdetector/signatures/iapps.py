"""
This signature containts test to see if the site is running on iApps.
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
    
    NAME = 'iApps'
    WEBSITE = 'http://www.iapps.com/'
    KNOWN_POSITIVE = 'http://www.iapps.com/'
    TECHNOLOGY = '.NET'

    def test_has_style_library(self, site):
        """
        iApps puts style sheets and Javascript in a 'Style%20Library' directory
        """
        
        if site.home_page.has_matching_tag('link', {'rel':'stylesheet','href':'Style\%20Library'}):
            return 1
        else:
            return 0
            
            
        
