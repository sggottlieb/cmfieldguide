from cmfieldguide.cmsdetector.signatures import BaseSignature



class Signature(BaseSignature):
    
    NAME = 'Drupal'

    def test_has_sites_path(self, url):
        """Has a /sites/all path in HTML."""
        return 0

    def test_has_node_class_on_body_tag(self, url):
        """Has a class containing 'node' on the BODY tag."""
        return 0
    
    def test_is_drupal_org(self,url):
        """
        This is kind of cheating
        """
        if url == 'http://drupal.org/':
            return 100
        else:
            return 0