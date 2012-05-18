"""
This signature contains tests to see if the site is running on Hippo CMS.
"""
__author__ = "Jeroen Reijn"
__copyright__ = "CM Fieldguide"
__credits__ = ["Jeroen Reijn",]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Jeroen Reijn"
__email__ = "j.reijn@onehippo.com"
__status__ = "Experimental"


from cmfieldguide.cmsdetector.signatures import BaseSignature

class Signature(BaseSignature):

    NAME = 'Hippo CMS'
    WEBSITE = 'http://www.onehippo.com/en/products/cms'
    KNOWN_POSITIVE = 'www.onehippo.com'
    TECHNOLOGY = 'JAVA'

    def test_binaries_file_paths(self, site):
        """
        Hippo CMS exposes image data generally from the binaries path.
        """
        
        if site.home_page.contains_any_pattern(
            ['/binaries/content/gallery/']
            ):
            return 1
        else:
            return 0
        
