"""
This signature containts test to see if the site is running on SilverStripe.
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
    
    NAME = 'SilverStripe'
    WEBSITE = 'http://www.silverstripe.com/'
    KNOWN_POSITIVE = 'http://www.silverstripe.com/'
    TECHNOLOGY = 'PHP'

    def test_login_redirect(self, site):
        """
        When trying to access the backend UI ("/admin"), SilverStripe will 
        redirect you to a login page under the URL /Security/login
        """
        
        if '/Security/login' in site.page_cache[site.url_stem + '/admin'].get_url:
            return 1
        else:
            return 0
        
