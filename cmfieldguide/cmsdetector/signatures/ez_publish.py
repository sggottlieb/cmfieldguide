from cmfieldguide.cmsdetector.signatures import BaseSignature



class Signature(BaseSignature):
    
    NAME = 'eZ Publish'
    WEBSITE = 'http://ez.no'
    KNOWN_POSITIVE = 'http://ez.no/'
    

    def test_has_sites_path(self, url):
        """
        eZ Publish sites usually have their design in an extension
        """
        
        pattern = "\"/extension/[\w|\-|_]*/design"
        
        if self.page_contains_pattern(url, pattern):
            return 1
        else:
            return 0    

    def test_has_sites_path(self, url):
        """
        eZ Publish ships with some default designs that are under the /design directory
        """

        pattern = "\"/design"

        if self.page_contains_pattern(url, pattern):
            return 1
        else:
            return 0
