from django.test import TestCase
from cmfieldguide.cmsdetector.signatures import BaseSignature
from cmfieldguide.cmsdetector.engine import get_cms_names


class TestBase(TestCase):
    sig = BaseSignature()
    
    def test_page_contains_pattern(self):
        url = "http://www.contenthere.net"
        pattern = "wp-content/themes/"
        self.assertTrue(self.sig.page_contains_pattern(url,pattern))
        
    def test_get_url_stem(self):
        """
        Tests that the URL stem method works
        """
        
        stem = 'http://www.acme.com'
        self.assertEqual(self.sig.get_url_stem(stem + '/foo/bar'), stem)
    
        
    def test_url_exists(self):
        good_url = 'http://www.google.com'
        bad_url = 'http://yomamma.blendinteractive.com'
        
        self.assertTrue(self.sig.url_exists(good_url))
        self.assertFalse(self.sig.url_exists(bad_url))


class TestSignatures(TestCase):
    
    
    def setUp(self):
        self.sig_list = []
        
        for cms_name in get_cms_names():
            self.sig_list.append(__import__('cmfieldguide.cmsdetector.signatures.' + cms_name, 
                fromlist='Signature').Signature())
    
    def test_metadata_override(self):
        """
        This test verifies that the metadata have been overridden
        """
        base = BaseSignature()
        
        for sig in self.sig_list:
            self.assertNotEqual(sig.NAME, base.NAME)
            self.assertNotEqual(sig.WEBSITE, base.WEBSITE)
            self.assertNotEqual(sig.KNOWN_POSITIVE, base.KNOWN_POSITIVE)
            
    def test_known_positives(self):
        """
        This test verifies that a confirmed site returns a positive
        """
        for sig in self.sig_list:
            if not sig.run(sig.KNOWN_POSITIVE):
                message = '%s should be return a true for %s' % (sig.KNOWN_POSITIVE, sig.NAME)
                self.fail(message)
            
            
    def test_known_negative(self):
        """
        This test verifies that a site not running the software returns
        a negative.
        """
        #We know that Google is not running any of these CMSs
        known_negative = 'http://www.google.com'
        
        for sig in self.sig_list:
            if sig.run(known_negative):
                message = 'We know %s is not a %s but the signature returned a positive' \
                    % (known_negative, sig.NAME)
                self.fail(message)
            
            
