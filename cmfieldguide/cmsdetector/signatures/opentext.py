"""
This signature contains test to see if the site is running on OpenText Web Site Management.
"""
__author__ = "Steven Brent"
__copyright__ = "CM Fieldguide"
__credits__ = ["Steven Brent","Markus Giesen"]
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
    TECHNOLOGY = 'BAKED'

    def test_has_identifying_publish_tag(self, site):
        """
        RedDot tends to inject comments that identify what version was used.
        """

        if site.home_page.contains_pattern("<!--\sPageID\s\d{1,6}\s-\spublished by RedDot"):
            """
            *Some* sites running version 7.x to 9.x of OpenText Web Site Management (formerly RedDot / RedDot Solutions) will contain this
            """
        elif site.home_page.contains_pattern("<!--\sPageID\s\d{1,6}\s-\spublished by Open Text Web Solutions"):
            """
            *Some* sites running version 9.x to 10.x of OpenText Web Site Management will contain this
            """
            return 1
        elif site.home_page.contains_pattern("<!--\sPageID\s\d{1,6}\s-\spublished by OpenText Web Site Management"):
            """
            Sites running version 11.x of OpenText Web Site Management will contain this
            """
            return 1
        else:
            return 0