from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'Drupal'
    WEBSITE = 'http://drupal.org'
    KNOWN_POSITIVE = 'http://drupal.org/'
    
    def test_is_not_web_forms(self, url):
        """
        Drupal is written in PHP.  It is highly unlikely that we would see any signs of
        .NET webforms.
        """
        
        
        if self.page_cache[url].is_dot_net_webforms():
            return -1
        else:
            return 0
        

    def test_has_sites_path(self, url):
        """
        Drupal sites manage themes under a path that 
        starts with /sites/all or sites/default.
        """
        
        if self.page_cache[url].contains_any_pattern(("/sites/all", "/sites/default")):
            return 1
        else:
            return 0
        
