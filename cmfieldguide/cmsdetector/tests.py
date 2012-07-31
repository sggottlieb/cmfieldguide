from django.test import TestCase
from cmfieldguide.cmsdetector.signatures import BaseSignature
from cmfieldguide.cmsdetector.page_tools import Page
from cmfieldguide.cmsdetector.forms import SiteForm
from cmfieldguide.cmsdetector.models import save_as_site_object
from cmfieldguide.cmsdetector.signatures import get_platform_names


class TestPage(TestCase):
    
    def test_page_contains_pattern(self):
        """
        Testing the contains_pattern method
        """
        page = Page("http://www.contenthere.net")
        self.assertTrue(page.contains_pattern("wp-content/themes/"))
        self.assertFalse(page.contains_pattern("wp content/themes/"))
        

    def test_php_credits(self):
        self.assertTrue(Page('http://drupal.org').has_php_credits())
        
        self.assertFalse(Page('http://www.blendinteractive.com').has_php_credits())
        
    def test_url_exists(self):
        """
        Tests that the exists function is working.
        """
        
        self.assertTrue(Page('http://www.google.com').exists())
        self.assertFalse(Page('http://www.contenthere.net/yomama').exists())
    
    def test_has_matching_tag(self):
        """
        Test our Beautiful Soup tag attribute method
        """
        
        page = Page('http://www.contenthere.net')
        self.assertTrue(page.has_matching_tag('div', {'id':'header', 'class':'row'}))
        self.assertFalse(page.has_matching_tag('div', {'id':'content', 'class':'foo'}))
        
        
    def test_has_tag_containing(self):
        """
        Tests our Beautiful Soup tag containing method
        """
        page = Page('http://www.contenthere.net')
        self.assertTrue(page.has_tag_containing_pattern('script','google-analytics'))
        self.assertFalse(page.has_tag_containing_pattern('script','gargle-analytics'))
        
    def test_get_title(self):
        page = Page('http://www.sethgottlieb.com')
        self.assertEquals(page.title, 'Seth Gottlieb : Seth Gottlieb : Home')
        
class TestSignaturePositives(TestCase):
    
    
    def setUp(self):
        self.sig_list = []
        for platform_name in get_platform_names():
            sig = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                fromlist='Signature')
            site = save_as_site_object(Page(sig.Signature.KNOWN_POSITIVE))
            self.sig_list.append(sig.Signature(site))
    
            
    def test_known_positives(self):
        """
        This test verifies that a confirmed site returns a positive
        """
        for sig in self.sig_list:
            if sig.confidence <= 0:
                message = '%s should be return a true for %s' % (sig.KNOWN_POSITIVE, sig.NAME)
                self.fail(message)

class TestSignatureNegatives(TestCase):


    def setUp(self):
        self.sig_list = []
        site = save_as_site_object(Page('http://www.google.com'))
        
        for platform_name in get_platform_names():
            sig = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                fromlist='Signature')
            self.sig_list.append(sig.Signature(site))

            
            
    def test_known_negative(self):
        """
        This test verifies that a site not running the software returns
        a negative.
        """
        
        for sig in self.sig_list:
            if sig.confidence > 0:
                message = '%s should be return a false for %s' % (self.known_negative, sig.NAME)
                self.fail(message)
            
            
