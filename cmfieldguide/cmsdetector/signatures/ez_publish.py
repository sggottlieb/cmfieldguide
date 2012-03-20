from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):
    
    NAME = 'eZ Publish'
    WEBSITE = 'http://ez.no'
    KNOWN_POSITIVE = 'http://ez.no/'
    
    
    def test_is_not_web_forms(self, url):
        """
        eZ Publish is written in PHP.  It is highly unlikely that we would see any signs of
        .NET webforms.
        """
        
        if self.page_cache[url].is_dot_net_webforms():
            return -1
        else:
            return 0
        

    def test_has_design_extension(self, url):
        """
        eZ Publish sites usually have their design in an extension
        """
        
        if self.page_cache[url].contains_pattern("\"/extension/[\w|\-|_]*/design"):
            return 1
        else:
            return 0
        
    def test_has_var_storage(self, url):
        """
        eZ Publish will often store images in a 'storage'
        directory located under a path.
        """
        
        if self.page_cache[url].contains_pattern("\"/var/[\w|\-|_]*/storage/images"):
            return 1
        elif self.page_cache[url].contains_pattern("\"/var/storage/images"):
            return 1
        else:
            return 0
        