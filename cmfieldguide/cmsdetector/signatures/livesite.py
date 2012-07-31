"""
This signature contains test to see if the site is running on TeamSite LiveSite.
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

    NAME = 'TeamSite LiveSite'
    WEBSITE = 'http://www.interwoven.com/'
    KNOWN_POSITIVE = 'http://www.deere.com/wps/dcom/en_US/'
    TECHNOLOGY = 'JAVA'

    def test_has_dot_page_extension(self, site):
        """
        TeamSite sites running LiveSite tend to have URLs that contain a .page extension
        """

        if site.home_page.has_matching_tag( 'a', { 'href': '\.page' } ):
            return 1
        else:
            return 0
            
