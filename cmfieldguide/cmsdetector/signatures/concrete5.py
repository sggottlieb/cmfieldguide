"""
This signature containts test to see if the site is running on Drupal.
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
    
    NAME = 'Concrete5'
    WEBSITE = 'http://www.concrete5.org/'
    KNOWN_POSITIVE = 'http://www.concrete5.org/'
    TECHNOLOGY = 'PHP'

    def test_has_bas_style(self, site):
        """
        Concrete5 by default come with a base stylesheet with
        a path like /concrete/css/ccm.base.css.
        """
        
        if site.home_page.contains_pattern('/concrete/css/ccm.base.css'):
            return 1
        else:
            return 0
        
