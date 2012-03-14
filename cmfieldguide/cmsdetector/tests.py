from django.test import TestCase
from cmfieldguide.cmsdetector.signatures import BaseSignature



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


class TestDrupal(TestCase):
    from cmfieldguide.cmsdetector.signatures.drupal import Signature as DrupalSignature
    sig = DrupalSignature()
    
    def test_verified_true_site(self):
        url = "http://drupal.org"
        self.assertEquals(self.sig.run(url),1)
        
    def test_verified_false_site(self):
        url = "http://plone.org/"
        self.assertEquals(self.sig.run(url),0)