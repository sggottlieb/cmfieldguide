"""
This signature containts test to see if the site is running on Jahia.
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

    NAME = 'Jahia'
    WEBSITE = 'http://www.jahia.com/cms/home.html'
    KNOWN_POSITIVE = 'http://www.jahia.com/cms/home.html'
    TECHNOLOGY = 'JAVA'

    def test_has_jahia_in_source(self, site):
        """
        Jahia sites litter the HTML with references to Jahia.  
        This can be in the form of Javascript variables or links.
        
        """
        
        if site.home_page.contains_pattern('jahia'):
            return 1
        else:
            return 0
        
        
 