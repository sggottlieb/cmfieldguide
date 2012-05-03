"""
This signature containts test to see if the site is running on Ingeniux.
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
    
    NAME = 'Ingeniux'
    WEBSITE = 'http://www.ingeniux.com/'
    KNOWN_POSITIVE = 'http://www.ingeniux.com/'
    TECHNOLOGY = '.NET'

    def test_has_prebuilt_directory(self, site):
        """
        Ingeniux puts style sheets and Javascript in a 'prebuilt' directory
        """
        
        if site.home_page.has_matching_tag('link', {'rel':'stylesheet','href':'prebuilt'}):
            return 1
        elif site.home_page.has_matching_tag('script', {'src':'prebuilt'}):
            return 1
        else:
            return 0
            
            
        
