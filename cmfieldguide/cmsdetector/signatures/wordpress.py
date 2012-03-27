"""
This signature tests for clues that a site is running on WordPress

"""


from cmfieldguide.cmsdetector.signatures import BaseSignature, get_url_stem


class Signature(BaseSignature):
    
    NAME = 'WordPress'
    WEBSITE = 'http://wordpress.org'
    KNOWN_POSITIVE = 'http://wordpress.org'
    TECHNOLOGY = 'PHP'
    
    def test_has_wp_login(self, url):
        """
        By default, Wordpress ships with a login page at /wp-login.php
        """
        
        if self.page_cache[get_url_stem(url) + '/wp-login.php'].contains_pattern('loginform'):
            return 100
        else:
            return 0
        
        
    def test_has_wp_theme(self, url):
        """
        Wordpress sites manage layouts and other formatting using style sheets in
        themes directory.
        """
        
        if self.page_cache[url].contains_pattern("wp-content/themes/"):
            return 1
        else:
            return 0
            
