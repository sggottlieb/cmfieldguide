"""
This signature containts test to see if the site is running on Plone.
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

    NAME = 'Plone'
    WEBSITE = 'http://plone.org'
    KNOWN_POSITIVE = 'http://plone.org'
    TECHNOLOGY = 'Python'

    def test_login_redirect(self, site):
        """
        Plone sends you to a special login page when you try to hit the manage area.
        """
        
        if 'acl_users' in site.page_cache[site.url_stem + '/manage'].get_url:
            return 1
        else:
            return 0
            
    