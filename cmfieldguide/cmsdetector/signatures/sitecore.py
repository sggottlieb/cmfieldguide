"""
This signature containts test to see if the site is running on Sitecore.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Timothy Davis",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "deane@blendinteractive.com"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'Sitecore'
    WEBSITE = 'http://www.sitecore.net/'
    KNOWN_POSITIVE = 'http://www.sitecore.net/'
    TECHNOLOGY = '.NET'

    def test_has_sitecore_password_recovery(self, site):
        """
        Sitecore ships with a password recovery page under this path: /sitecore/login/passwordrecovery.aspx
        """
        
        if site.page_cache[site.url_stem + '/sitecore/login/passwordrecovery.aspx'].contains_pattern('/sitecore/login/logo\.png'):
            return 1
        else:
            return 0
            
    