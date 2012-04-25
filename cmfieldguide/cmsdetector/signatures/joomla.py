"""
This signature containts test to see if the site is running on Joomla.
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
    
    NAME = 'Joomla'
    WEBSITE = 'http://joomla.org'
    KNOWN_POSITIVE = 'http://joomla.org/'
    TECHNOLOGY = 'PHP'

    def test_has_administrator_login(self, site):
        """
        Joomla! sites have a management area under the URL '/adminstrator'.
        
        If you go to this URL, you should see a login page.
        """
        login_page = site.page_cache[site.url_stem + '/administrator']
        
        if login_page.status_code != 404 and login_page.has_matching_tag( 'input', { 'name': 'username'} ):
            return 1
        else:
            return 0
        
