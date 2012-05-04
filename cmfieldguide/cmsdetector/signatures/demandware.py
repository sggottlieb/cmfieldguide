"""
This signature containts test to see if the site is running on DemandWare.
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

    NAME = 'Demandware'
    WEBSITE = 'http://www.demandware.com/'
    KNOWN_POSITIVE = 'http://www.starbucksstore.com/'
    TECHNOLOGY = 'JAVA'

    def test_uses_demandware_cdn(self, site):
        """
        Style sheets and images are hosted on Demandware's CDN
        """
        pattern = 'demandware\.edgesuite\.net'
        if site.home_page.has_matching_tag('link', {'rel':'stylesheet','href':pattern}):
            return 1
        elif site.home_page.has_matching_tag('img', {'src':pattern}):
            return 1
        else:
            return 0
            
    