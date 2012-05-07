"""
This signature containts test to see if the site is running on Hannon Hill.
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
    
    NAME = 'Hannon Hill Cascade Server'
    WEBSITE = 'http://www.hannonhill.com/'
    KNOWN_POSITIVE = 'http://www.hannonhill.com/'
    TECHNOLOGY = 'Baked'

    def test_has_analytics_marketing_code(self, site):
        """
        Newer implementations of Hannon Hill typically ship 
        with an 'Analytics and Inbound Marketing' service that
        requires some Javascript variables in the page.
        """
        
        if site.home_page.has_tag_containing_pattern('script','sAId') and \
            site.home_page.has_tag_containing_pattern('script','sCId'):
            return 1
        else:
            return 0
        
