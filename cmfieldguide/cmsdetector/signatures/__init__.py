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
import pkgutil

from cmfieldguide.cmsdetector.models import PlatformSiteTest, TestResult


def namify(m):
    """Turns a test name into a name"""
    
    return ' '.join(m.split('_')[1:]).title()

def get_platform_names():
    names = []

    
    for importer, modname, ispkg in pkgutil.iter_modules(__path__):
        names.append(modname)

    return names


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
    
    def __init__(self, site):
        """
        Runs through all of the test methods (identified by beginning
        with the string "test") and returns a confidence score.
        """
        confidence_score = 0
        test_count = 0
        
        pt = PlatformSiteTest.objects.create(
            site = site,
            platform_name = self.NAME,
            platform_website = self.WEBSITE,
            confidence = 0,
            
        )
        
        if self.TECHNOLOGY == '.NET' and not site.page_cache[site.url].is_dot_net_webforms():
            pt.explanation = 'This site cannot be %s because it is built using .NET technology' % self.NAME
            
            
        elif self.TECHNOLOGY not in ('PHP','Baked') and site.page_cache[site.url].has_php_credits():
            pt.explanation = 'This site cannot be %s because it is built using PHP technology' % self.NAME
            
        
        else:
            for m in dir(self):
                if m.startswith('test'):
                    test = getattr(self, m)
                    tr = TestResult.objects.create(
                        test_run = pt,
                        name = namify(m),
                        result = test(site),
                        explanation = test.__doc__
                    )
                    test_count += 1
                    confidence_score += tr.result
            pt.confidence = (confidence_score/float(test_count)) * 100
        
            
            if pt.confidence > 75:
                pt.explanation = 'This site is probably running %s' % self.NAME
            else:
                pt.explanation = 'This site is probably not running  %s' % self.NAME
        
        self.confidence = pt.confidence
        pt.save()    
        
    