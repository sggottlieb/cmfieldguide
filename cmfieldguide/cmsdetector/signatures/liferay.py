"""
This signature containts test to see if the site is running on Liferay.
"""
__author__ = "Seth Gottlieb"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb"]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'Liferay'
    WEBSITE = 'http://www.liferay.com/'
    KNOWN_POSITIVE = 'http://www.liferay.com/'
    TECHNOLOGY = 'JAVA'

    def test_has_css_jsp(self, site):
        """
        Liferay has a CSS JSP that loads style sheets based on some query string arguments
        http://www.sesamestreet.org/html/portal/css.jsp?browserId=other&themeId=sesamestreet_WAR_sesamestreettheme&colorSchemeId=01&minifierType=css&t=1335842976000
        
        """
        
        if site.home_page.has_matching_tag('link',{'rel':'stylesheet','href':'css\.jsp.*themeId'}):
            return 1
        else:
            return 0
    