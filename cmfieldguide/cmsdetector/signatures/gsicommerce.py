"""
This signature containts test to see if the site is running on GSI Commerce.
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

    NAME = 'GSI Commerce'
    WEBSITE = 'http://www.gsicommerce.com/'
    KNOWN_POSITIVE = 'http://www.bathandbodyworks.com/'
    TECHNOLOGY = 'JAVA'

    def test_imageg_image_storage(self, site):
        """
        GSI Commerce Sites tend to host their images, css, and javascript on a subdomain of imageg.net
        
        """
        
        if site.home_page.has_matching_tag('img',{'src':'imageg\.net'}):
            return 1
        elif site.home_page.has_matching_tag('script',{'src':'imageg\.net'}):
            return 1
        elif site.home_page.has_matching_tag('link',{'href':'imageg\.net'}):
            return 1
        else:
            return 0
        
        
 