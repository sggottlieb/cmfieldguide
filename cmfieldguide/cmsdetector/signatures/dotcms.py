"""
This signature containts test to see if the site is running on dotCMS.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb", 'Adriaan Bloem']
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'dotCMS'
    WEBSITE = 'http://dotcms.com/'
    KNOWN_POSITIVE = 'http://dotcms.com/'
    TECHNOLOGY = 'JAVA'

    def test_has_dot_extension(self, site):
        """
        dotCMS pages natively have a .dot extension although this is masked
        with directories and an index.dot
        
        """
        
        if site.home_page.contains_pattern('\.dot'):
            return 1
        else:
            return 0
        
        