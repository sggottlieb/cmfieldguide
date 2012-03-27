"""
This signature containts test to see if the site is running on Hannon Hill.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb",]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'Hannon Hill Cascade Server'
    WEBSITE = 'http://www.hannonhill.com/'
    KNOWN_POSITIVE = 'http://www.hannonhill.com/'
    TECHNOLOGY = 'Baked'

    def test_has_underscore_files_directory(self, url):
        """
        Hannon Hill sites tend to template resources such as CSS and images 
        stored in a _files directory.
        
        
        
        """
        
        if self.page_cache[url].contains_pattern('_files'):
            return 1
        else:
            return 0
        
