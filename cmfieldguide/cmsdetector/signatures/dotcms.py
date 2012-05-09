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
        
        dot_url = site.url.rstrip('/') + '/index.dot'
        
        if site.url.endswith('.dot'):
            return 1
        elif site.page_cache[dot_url].status_code == 200 \
            and site.page_cache[dot_url].get_url == dot_url:
            return 1
        else:
            return 0
    