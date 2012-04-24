import pickle
from django.db import models
from page_tools import *

def save_as_site_object(page):
    if page.url:
        site = Site.objects.create(
            url = page.url,
            title = page.get_title(),
            html = page.html,
            status_code = page.status_code,
            headers = pickle.dumps(page.headers),
            geturl = page.geturl,
        )
        site.page_cache[page.url] = page
        return site
    else:
        return None

class PlatformSiteTest(models.Model):
    site = models.ForeignKey('Site')
    platform_name = models.CharField(max_length=100)
    platform_website = models.URLField()
    confidence = models.IntegerField()
    explanation = models.TextField(blank=True, null=True)
    visitor_rejects = models.BooleanField(default=False)
    
    class Meta:
        ordering = ["-site__date_time", "platform_name"]
    
    def __unicode__(self):
        return u"%s test for %s on %d/%d/%d" % (
            self.platform_name,
            self.site.url,
            self.site.date_time.month,
            self.site.date_time.day,
            self.site.date_time.year
            
        
        )

    def results(self):
        return TestResult.objects.filter(test_run=self)


class TestResult(models.Model):
    test_run = models.ForeignKey('PlatformSiteTest')
    name = models.CharField(max_length=100)
    result = models.IntegerField()
    explanation = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s: %s on %d/%d/%d" % (self.test_run.platform_name, 
            self.name, 
            self.test_run.site.date_time.month,
            self.test_run.site.date_time.day,
            self.test_run.site.date_time.year)

class Site(models.Model):
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    html = models.TextField(blank=True, null=True)
    status_code = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    headers = models.TextField(blank=True, null=True)
    geturl = models.CharField(blank=True, null=True, max_length=200)
    
    def __unicode__(self):
        return u"%s on %d/%d/%d" % (self.url, 
            self.date_time.month,
            self.date_time.day,
            self.date_time.year
        )
    
    @property
    def url_stem(self):
        """
        Returns the stem of the URL.  

        For example, if the URL is http://www.acme.com/foo/bar, 

        The stem would be http://www.acme.com

        """

        return '/'.join(self.url.split('/')[:3])
    
    @property
    def home_page(self):
        """
        Returns the page that the user submitted as the
        home page.
        """
        return self.page_cache[self.url]
    
    @property
    def root_page(self):
        """
        Returns the page at the site root
        
        """
        return self.page_cache[self.url_stem]    

    def platforms(self):
        return PlatformSiteTest.objects.filter(site=self).order_by('-confidence')

    page_cache = PageCache()

    
    

    



   