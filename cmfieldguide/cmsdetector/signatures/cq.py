"""
This signature containts test to see if the site is running on Magnolia.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Robb Winkle",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'Adobe CQ'
    WEBSITE = 'http://www.adobe.com/products/cq.html'
    KNOWN_POSITIVE = 'http://www.gm.com'
    TECHNOLOGY = 'JAVA'

    def test_file_paths(self, site):
        """
        CQ likes to store CSS and JS in /etc/designs and will have references to paths
        like /libs/cq or /libs/wcm or /content/dam
        
        """
        
        if site.home_page.contains_any_pattern(
            ['/etc/designs/','/libs/cq/', '/libs/wcm/', '/content/dam/']
            ):
            return 1
        else:
            return 0
        
        
 