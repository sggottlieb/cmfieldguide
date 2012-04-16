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
    
    NAME = 'Drupal'
    WEBSITE = 'http://drupal.org'
    KNOWN_POSITIVE = 'http://drupal.org/'
    TECHNOLOGY = 'PHP'

    def test_has_sites_path(self, site):
        """
        Drupal sites manage themes under a path that 
        starts with /sites/all or sites/default.
        """
        
        if site.home_page.contains_any_pattern(("/sites/all", "/sites/default")):
            return 1
        else:
            return 0
        
