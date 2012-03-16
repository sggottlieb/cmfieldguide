"""
This signature tests for clues that a site is running on EPiServer

"""


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'EPiServer'
    WEBSITE = 'http://episerver.com'
    KNOWN_POSITIVE = 'http://episerver.com'

    def test_has_episerverlogin(self, url):
        """
        EPiServer sites usually have a login page under the url /util/login.aspx
        """

        if self.url_exists(self.get_url_stem(url) + '/util/login.aspx'):
            return 100

    def test_is_dot_net_webforms(self, url):
        """
        EPiServer is a .Net CMS
        """

        if self.is_dot_net_webforms(self, url):
            return 1