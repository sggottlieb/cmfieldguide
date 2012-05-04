"""
This signature containts test to see if the site is running on Websphere Commerce.
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

    NAME = 'Websphere Commerce'
    WEBSITE = 'http://www-01.ibm.com/software/genservers/commerceproductline/'
    KNOWN_POSITIVE = 'http://store.sony.com/'
    TECHNOLOGY = 'JAVA'

    def test_has_wcs_url(self, site):
        """
        All the pages of a Webshpere Commerce website have a URL that contains "wcs/stores/servlet"
        """
        pattern = 'wcs/stores/servlet'
        if pattern in site.home_page.url:
            return 1
        elif pattern in site.home_page.get_url:
            return 1
        else:
            return 0
            
    