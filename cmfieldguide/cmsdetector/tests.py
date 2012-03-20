from django.test import TestCase
from cmfieldguide.cmsdetector.signatures import BaseSignature, Page, get_url_stem, PageCache
from cmfieldguide.cmsdetector.engine import get_platform_names


class TestPage(TestCase):
    
    def test_page_contains_pattern(self):
        url = "http://www.contenthere.net"
        pattern = "wp-content/themes/"
        page = Page(url)
        self.assertTrue(page.contains_pattern(pattern))
        
    def test_get_url_stem(self):
        """
        Tests that the URL stem method works
        """
        
        stem = 'http://www.acme.com'
        self.assertEqual(get_url_stem(stem + '/foo/bar'), stem)
    
        
    def test_url_exists(self):
        """
        Tests that the exists function is working.
        """
        
        good_page = Page('http://www.google.com')
        bad_page = Page('http://www.contenthere.net/yomama')
        
        self.assertTrue(good_page.exists())
        self.assertFalse(bad_page.exists())


class TestSignaturePositives(TestCase):
    
    
    def setUp(self):
        self.sig_list = []
        page_cache = PageCache()
        for platform_name in get_platform_names():
            sig = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                fromlist='Signature')
            self.sig_list.append(sig.Signature(sig.Signature.KNOWN_POSITIVE, page_cache))
    
            
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
        page_cache = PageCache()
        
        self.known_negative = 'http://www.google.com'
        
        for platform_name in get_platform_names():
            sig = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                fromlist='Signature')
            self.sig_list.append(sig.Signature(self.known_negative, page_cache))

            
            
    def test_known_negative(self):
        """
        This test verifies that a site not running the software returns
        a negative.
        """
        
        for sig in self.sig_list:
            if sig.confidence > 0:
                message = '%s should be return a false for %s' % (self.known_negative, sig.NAME)
                self.fail(message)
            
            
