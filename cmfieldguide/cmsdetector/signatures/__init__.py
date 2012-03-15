__author__ = 'Deane Barker'

import urllib2
import re

class BaseSignature(object):
    
    NAME = 'Base Signature Class.  OVERRIDE'
    WEBSITE = 'http://www.acme.org OVERRIDE'
    KNOWN_POSITIVE = 'http://www.acme.org OVERRIDE'
    
    def run(self, url):
        """
        Runs through all of the test methods (identified by beginning
        with the string "test") and returns a confidence score.
        """
        
        confidence_score = 0
        
        tests = []
        for m in dir(self):
            if m.startswith('test'):
                tests.append(getattr(self, m))
        
        if not len(tests):
            raise SystemError("There are no tests!")
                
        for test in tests:
            conf = test(url)        
            if conf == 100:
                # This test is absolutely certain
                return 1
            elif conf > 0:
                # Test found a clue
                confidence_score += 1
            elif conf < 0:
                # Test ruled out this CMS
                confidence_score = 0
                break
        
        return confidence_score/len(tests)
        
    def get_url_stem(self, url):
        """
        Returns the stem of the URL.  
        
        For example, if the URL is http://www.acme.com/foo/bar, 
        
        The stem would be http://www.acme.com
        
        """
        
        return '/'.join(url.split('/')[:3])
        
    def page_contains_pattern(self, url, pattern):
        """
        Returns True if the given page contains a particular string.
        """
        result = False
        rgx = re.compile(pattern)
        
        try:
            page = urllib2.urlopen(url)
            for line in page:
                if rgx.search(line):
                    result = True
                    break
        
            page.close()
        except urllib2.HTTPError, IOError:
            pass
        
        return result
        
    def url_exists(self, url):
        """
        Returns True if the URL exists
        
        """
        result = False
        
        try:
            page = urllib2.urlopen(url, timeout=2)
            if page.getcode() in (200,):
                result = True
            page.close()
        except IOError:
            pass
        
        return result
        
    
class SampleSignature(BaseSignature):
    """
    SampleSignature is a very basic example of how to extend BaseSignature
    
    """
    
    def test_anything(self, url):
        """
        Just verifies that the url string is not null
        
        """
        if url:
            return True
        else:
            return False