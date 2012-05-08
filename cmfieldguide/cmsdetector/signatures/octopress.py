"""
This signature containts test to see if the site is running on Octopress.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb","Wes Winham"]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'Octopress'
    WEBSITE = 'http://octopress.org/'
    KNOWN_POSITIVE = 'http://octopress.org/'
    TECHNOLOGY = 'Baked'

    def test_has_css_version_querystring(self, site):
        """
        Octopress ships with an octopress.js file
        """
        
        if site.page_cache[site.url + '/javascripts/octopress.js'].contains_pattern('getNav'):
            return 1
        else:
            return 0
            
            
        
