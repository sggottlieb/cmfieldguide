"""
This signature tests for clues that a site is running on EPiServer

"""


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
        
        if self.page_cache[get_url_stem(url) + '/util/login.aspx'].exists():
            return 100
        else:
            return 0
            
    