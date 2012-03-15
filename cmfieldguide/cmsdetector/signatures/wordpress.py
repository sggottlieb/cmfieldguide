"""
This signature tests for clues that a site is running on WordPress

"""


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):
    
    NAME = 'WordPress'
    WEBSITE = 'http://wordpress.org'
    KNOWN_POSITIVE = 'http://wordpress.org'

    def test_has_wplogin(self, url):
        """
        Wordpress sites usually have a login page under the url /wp-login.php 
        """
        
        if self.page_contains_pattern(self.get_url_stem(url) + '/wp-login.php', 'loginform'):
            return 100

    def test_has_wptheme(self, url):
        """
        Wordpress sites manage layouts and other formatting using style sheets in
        themes directory.
        """
        
        if self.page_contains_pattern(url, "wp-content/themes/"):
            return 100