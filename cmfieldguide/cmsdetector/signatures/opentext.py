"""
This signature contains test to see if the site is running on OpenText Web Site Management.
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

    NAME = 'OpenText Web Site Management'
    WEBSITE = 'http://websolutions.opentext.com'
    KNOWN_POSITIVE = 'http://websolutions.opentext.com'
    TECHNOLOGY = '.NET'

    def test_has_identifying_publish_tag(self, site):
        """
        *Some* sites running *some* versions of OpenText Web Site Management will contain this
        """

        if site.home_page.contains_pattern("<!--\sPageID\s\d{1,6}\s-\spublished by Open Text Web Solutions"):
            return 1
        else:
            return 0
            
