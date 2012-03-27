"""
This signature containts test to see if the site is running on Umbraco.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature, get_url_stem


class Signature(BaseSignature):
    
    NAME = 'Umbraco'
    WEBSITE = 'http://umbraco.com/'
    KNOWN_POSITIVE = 'http://umbraco.com/'
    TECHNOLOGY = '.NET'

    def test_has_umbraco_login(self, url):
        """
        Umbraco sites have a login page under the URL '/umbraco/login.aspx'.

        """
        
        if self.page_cache[get_url_stem(url) + '/umbraco/login.aspx'].contains_pattern('Umbraco'):
            return 1
        else:
            return 0
        
