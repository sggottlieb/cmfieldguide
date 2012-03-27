"""
This signature containts test to see if the site is running on EPiServer.
"""
__author__ = "Deane Barker"
__copyright__ = "CM Fieldguide"
__credits__ = ["Deane Barker",]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "deane@blendinteractive.com"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature, get_url_stem

class Signature(BaseSignature):

    NAME = 'EPiServer'
    WEBSITE = 'http://episerver.com'
    KNOWN_POSITIVE = 'http://episerver.com'
    TECHNOLOGY = '.NET'

    def test_has_episerver_login(self, url):
        """
        EPiServer sites usually have a login page under the url /util/login.aspx.
        
        The existence of this page yields a high confidence of EPiServer being used.
        """
        
        if self.page_cache[get_url_stem(url) + '/util/login.aspx'].contains_pattern('ctl00_FullRegion_LoginControl_UserName'):
            return 1
        else:
            return 0
            
    