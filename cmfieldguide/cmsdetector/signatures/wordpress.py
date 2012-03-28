"""
This signature containts test to see if the site is running on Wordpress.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


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
            return 1
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
            
