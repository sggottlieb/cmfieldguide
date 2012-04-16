"""
This signature containts test to see if the site is running on Umbraco.
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
    
    NAME = 'Umbraco'
    WEBSITE = 'http://umbraco.com/'
    KNOWN_POSITIVE = 'http://umbraco.com/'
    TECHNOLOGY = '.NET'

    def test_has_umbraco_login(self, site):
        """
        Umbraco sites have a login page under the URL '/umbraco/login.aspx'.

        """
        
        if site.page_cache[site.url_stem + '/umbraco/login.aspx'].contains_pattern('<input name="lname"'):
            return 1
        else:
            return 0
        
