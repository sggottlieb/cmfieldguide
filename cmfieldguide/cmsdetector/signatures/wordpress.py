from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):
    
    NAME = 'WordPress'

    def test_has_wpadmin(self, url):
        """Has a valid URL at wp-admin."""
        return 0

    def test_has_wptheme(self, url):
        """Has a WP-Theme directory."""
        if self.page_contains_pattern(url, "wp-content/themes/"):
            return 100