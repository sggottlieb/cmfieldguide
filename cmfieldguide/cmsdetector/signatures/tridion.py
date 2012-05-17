"""
This signature containts test to see if the site is running on Tridion.
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
    
    NAME = 'Tridion'
    WEBSITE = 'http://www.sdl.com/en/wcm/'
    KNOWN_POSITIVE = 'http://www.klm.com/travel/nl_nl/index.htm'
    TECHNOLOGY = 'Baked'

    def test_has_tcm_attribute(self, site):
        """
        Tridion often adds a "tcm" attribute on binaries.
        """
        
        if site.home_page.has_matching_tag('img', {'tcmuri':'tcm'}):
            return 1
        elif site.home_page.has_matching_tag('img', {'src':'tcm'}):
            return 1
        else:
            return 0
        
