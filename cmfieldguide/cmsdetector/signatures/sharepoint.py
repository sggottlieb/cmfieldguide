"""
This signature containts test to see if the site is running on SharePoint.
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
    
    NAME = 'Sharepoint'
    WEBSITE = 'http://sharepoint.microsoft.com/en-us/Pages/default.aspx'
    KNOWN_POSITIVE = 'http://www.ferrari.com/'
    TECHNOLOGY = '.NET'

    def test_has_sharepoint_error_page(self, site):
        """
        SharePoint has a distinct error page under /_layouts/error.aspx.
        """
        
        if site.page_cache[site.url_stem+'/_layouts/error.aspx'].contains_pattern('Troubleshoot issues with Microsoft SharePoint Foundation'):
            return 1
        else:
            return 0
        
