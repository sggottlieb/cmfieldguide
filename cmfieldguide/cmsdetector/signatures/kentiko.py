"""
This signature containts test to see if the site is running on Kentico.
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

    NAME = 'Kentiko'
    WEBSITE = 'http://www.kentico.com'
    KNOWN_POSITIVE = 'http://www.kentico.com'
    TECHNOLOGY = '.NET'

    def test_has_getcss(self, site):
        """
        Kentico has a GetCSS page that retrieve stylesheets by name.
        """
        if site.home_page.has_matching_tag( 'link', { 'rel': 'stylesheet', 'href': 'GetCSS\.aspx\?stylesheetname' } ):
            return 1
        else:
            return 0
            
    def test_has_kentico_login_page(self, site):
        """
        Kentico sites often have a login page under /CMSPages/logon.aspx
        """

        if site.page_cache[site.url_stem + '/CMSPages/logon.aspx'].has_matching_tag(tag_name='input',
                attributes={'name':'Login1\$UserName'}):
            return 1
        else:
            return 0
