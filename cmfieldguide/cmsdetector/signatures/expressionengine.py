"""
This signature containts test to see if the site is running on ExpressionEngine.
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
    
    NAME = 'ExpressionEngine'
    WEBSITE = 'http://expressionengine.com/'
    KNOWN_POSITIVE = 'http://expressionengine.com/'
    TECHNOLOGY = 'PHP'

    def test_has_css_loader_script(self, site):
        """
        ExpressionEngine loads CSS files with a query string off the root of the site like
        ?css=something.css
        """
        
        passed_url = site.url.replace('.','\.')
        root_url = site.url_stem.replace('.','\.')
        get_url = site.geturl.replace('.','\.')
        
        if site.home_page.has_matching_tag('link', {'rel':'stylesheet','href': passed_url +'/\?css=\w+[/\.]'}):
            return 1
        elif site.home_page.has_matching_tag('link', {'rel':'stylesheet','href': root_url +'/\?css=\w+[/\.]'}):
            return 1
        elif site.home_page.has_matching_tag('link', {'rel':'stylesheet','href': get_url +'/\?css=\w+[/\.]'}):
            return 1
        else:
            return 0
        
