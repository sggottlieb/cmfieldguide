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
    KNOWN_POSITIVE = 'http://www.carlosboozer5.com/'
    TECHNOLOGY = 'PHP'

    def test_has_login_under_manager(self, site):
        """
        Many Modx sites have the backend under "/manager."  If you go to this page, you will
        get a login form that will probably say Modx.
        """
        
        if site.page_cache[site.url_stem + "/manager"].contains_pattern('modx'):
            return 1
        else:
            return 0
            
            
        
