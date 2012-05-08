"""
This signature contains test to see if the site is running on elcomCMS.
"""
__author__ = "Steven Brent"
__copyright__ = "CM Fieldguide"
__credits__ = ["Steven Brent",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Steven Brent"
__email__ = "scbrent@gmail.com"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'elcomCMS'
    WEBSITE = 'http://elcomcms.com'
    KNOWN_POSITIVE = 'http://elcomcms.com/'
    TECHNOLOGY = '.NET'
    
    def test_has_cmlogin_aspx(self, site):
        """
        Look for the standard elcomCMS login page
        """
        if site.page_cache[site.url_stem + '/cmlogin.aspx'].contains_pattern('Login'):
            return 1
        else:
            return 0

    def test_has_uploaded_styles_path(self, site):
        """
        Look for the standard elcomCMS path to CSS
        """

        if site.home_page.contains_pattern("/UserUploadedStyles/"):
            return 1
        else:
            return 0
            
