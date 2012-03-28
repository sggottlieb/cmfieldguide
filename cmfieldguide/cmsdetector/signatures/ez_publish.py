"""
This signature containts test to see if the site is running on eZ Publish.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):
    
    NAME = 'eZ Publish'
    WEBSITE = 'http://ez.no'
    KNOWN_POSITIVE = 'http://ez.no/'
    TECHNOLOGY = 'PHP'
    
    
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
        