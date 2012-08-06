"""
This signature containts test to see if the site is running on TYPO3.
"""
__author__ = "Markus Giesen"
__copyright__ = "CM Fieldguide"
__credits__ = ["Markus Giesen"]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Markus Giesen"
__email__ = "info@markusgiesen.de"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature


class Signature(BaseSignature):
    
    NAME = 'TYPO3'
    WEBSITE = 'http://typo3.org'
    KNOWN_POSITIVE = 'http://typo3.org'
    TECHNOLOGY = 'PHP'
    
	def test_has_identifying_publish_tag(self, site):
        """
        All the pages of a TYPO3 website have a big HTML comment at the top that contains "This website is powered by TYPO3"
        """

        if site.home_page.contains_pattern("<!--\sPageID\s\d{1,6}\s-\sThis website is powered by TYPO3"):
            return 1
        else:
            return 0
	
    def test_has_identifying_meta_tag(self, site):
        """
        All the pages of a TYPO3 website have a meta tag that contains <meta name="generator" content="TYPO3
        """
		
        pattern = 'TYPO3'
        if site.home_page.has_matching_tag('meta', {'name':'generator','content':pattern}):
            return 1
        else:
            return 0
            
