from cmfieldguide.cmsdetector.signatures import BaseSignature



class Signature(BaseSignature):
    
    NAME = 'Drupal'
    WEBSITE = 'http://drupal.org'
    KNOWN_POSITIVE = 'http://drupal.org/'
    

    def test_has_sites_path(self, url):
        """
        Drupal sites manage themes under a path that 
        starts with /sites/all or sites/default.
        """
        if self.page_contains_pattern(url, "/sites/all"):
            return 1
        elif self.page_contains_pattern(url, "/sites/default"):
            return 1
        else:
            return 0    

