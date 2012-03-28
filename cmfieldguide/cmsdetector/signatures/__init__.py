from __future__ import division

"""
This module contains base and helper functionality to make
platform signatures easier to write.
"""
__author__ = "Seth Gottlieb and Deane Barker"
__copyright__ = "CM Fieldguide"
__credits__ = ["Seth Gottlieb", "Deane Barker"]
__license__ = "Unlicense"
__version__ = "0.1"
__maintainer__ = "Seth Gottlieb"
__email__ = "sgottlieb@alumni.duke.edu"
__status__ = "Experimental"


import urllib2
import re


def get_url_stem(url):
    """
    Returns the stem of the URL.  
    
    For example, if the URL is http://www.acme.com/foo/bar, 
    
    The stem would be http://www.acme.com
    
    """
    
    return '/'.join(url.split('/')[:3])

def namify(m):
    """Turns a test name into a name"""
    
    return ' '.join(m.split('_')[1:]).title()


class PageCache(dict):
    """
    This is just a basic dictionary object.  I am 
    overriding it to add a new page if the dictionary 
    doesn't already have a page for the URL.
    """
    def __init__(self, *args):
        dict.__init__(self, args)
    
    def __getitem__(self, key):
        """"
        Retrieves a page. If the page has already
        been retrieved, this method pulls it from cache.
        """
        if not key in dict.keys(self):
            dict.__setitem__(self, key, Page(key))
    
        return dict.__getitem__(self, key)

class Page(object):
    """
    This class is used to read a page from a URL and store its contents.
    It also contains methods for examining the contents of a page.
    """
    html = ''
    status_code = 0
    
    
    def __init__(self, url):
        
        self.url = url
        
        try:
            page = urllib2.urlopen(url, timeout=2)
        except urllib2.HTTPError, error:
            page = error
        except IOError:
            page = None
            
        if page:
            self.status_code = page.getcode()
            self.headers = page.headers
            
            for line in page.readlines():
                self.html += line    
            page.close()
            
    def exists(self):
        """
        Return True if a request for this page 
        returned a status code in the 200s
        """
        
        if str(self.status_code)[0] == '2':
            return True
        else:
            return False  
    
    def contains_pattern(self, pattern, ignorecase=False):
        """
        Returns True if the given page contains a particular string.
        """
        result = False
        if ignorecase:
            rgx = re.compile(pattern, re.IGNORECASE)
        else:
            rgx = re.compile(pattern)
        
        if self.html and rgx.search(self.html):
                result = True
        
        return result 

    def contains_any_pattern(self, patterns):
        """
        Returns a True if any of the patterns are found in the page
        """
        
        for pattern in patterns:
            if self.contains_pattern(pattern):
                return True
        
        return False
        
        
    def contains_all_patterns(self,patterns):
        """
        Returns a false unless all of the patterns are found in the page
        """
        
        for pattern in patterns:
            if not self.contains_pattern(pattern):
                return False
        
        return True
        
    
    def is_dot_net_webforms(self):
        """
        Returns True is the URL has .Net WebForm markers.
        """
        result = False

        if 'x-powered-by' in self.headers and self.headers['x-powered-by'] == 'ASP.NET':
            result = True

        if self.contains_any_pattern(('id="aspnetform"','ct100_','name="__VIEWSTATE"')):
            result = True

        return result

    def has_php_credits(self):
        """
        Checks for the easter egg where the PHP credits page 
        appears when you add the query string:
        ?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000
        """
        credits_page = Page(self.url + "?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000")
        return credits_page.contains_pattern('PHP Credits') 

class BaseSignature(object):
    """
    This is the base class from which all platform-specific signatures
    should extend.  When extending BaseSignature, please override the NAME, 
    WEBSITE, TECHNOLOGY, AND KNOWN_POSITIVE constants.
    """
    
    # Used to display the name of the platform this signature represents
    NAME = 'Base Signature Class.  OVERRIDE'
    
    # The website of the platform.  Often we assume that this website 
    # is running the platform
    WEBSITE = 'http://www.acme.org OVERRIDE'
    
    # Set this to PHP, .NET, Java, Python, or Ruby
    TECHNOLOGY = 'unknown'
    
    # This is a site that you know is running the platform.
    # Our unit tests check to make sure the signature returns
    # a positive for this site.
    KNOWN_POSITIVE = 'http://www.acme.org OVERRIDE'
    
    def __init__(self, url, page_cache):
        """
        Runs through all of the test methods (identified by beginning
        with the string "test") and returns a confidence score.
        """
        
        self.results = []
        confidence_score = 0
        self.page_cache = page_cache
        self.explanation = ''
        
        if self.TECHNOLOGY != '.NET' and self.page_cache[url].is_dot_net_webforms():
            self.explanation = 'This site cannot be %s because it is built using .NET technology' % self.NAME
            self.confidence = 0
            
        elif self.TECHNOLOGY not in ('PHP','Baked') and self.page_cache[url].has_php_credits():
            self.explanation = 'This site cannot be %s because it is built using PHP technology' % self.NAME
            self.confidence = 0
        
        else:
            for m in dir(self):
                if m.startswith('test'):
                    test = getattr(self, m)
                    result = {
                        'name':namify(m),
                        'score':test(url),
                        'description':test.__doc__
                        }
                    self.results.append(result)
            
            self.confidence = self.get_confidence()
            if self.confidence > 75:
                self.explanation = 'This site is probably running %s' % self.NAME
            else:
                self.explanation = 'This site is probably not running  %s' % self.NAME
            
        
    def get_confidence(self):
        score = 0
        
        for result in self.results:
            if result['score'] == 1:
                score += 1
            elif result['score'] == 100:
                return 100
            elif result['score'] < 0:
                return 0
                
        return (score/len(self.results)) * 100