"""
This signature containts test to see if the site is running on Magnolia.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb", 'Adriaan Bloem']
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'Magnolia CMS'
    WEBSITE = 'http://www.magnolia-cms.com/'
    KNOWN_POSITIVE = 'http://www.magnolia-cms.com/'
    TECHNOLOGY = 'JAVA'

    def test_has_login_page(self, site):
        """
        Magnolia has a login page under /.magnolia
        
        """
        
        
        login_page = site.page_cache[site.url_stem + '/.magnolia']
        
        if login_page.status_code != 404 and login_page.has_matching_tag('input', { 'name': 'mgnlUserId'} ):
            return 1
        else:
            return 0
    
    def test_has_static_image_dir(self, site):
        """
        Magnolia likes to store images in directories like /.imaging/stk 
        """
        
        if site.home_page.contains_pattern('\.imaging/stk/'):
            return 1
        elif site.home_page.contains_pattern('/magnoliaAssets/'):
            return 1
        else:
            return 0    
    