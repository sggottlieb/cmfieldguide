import signatures
import pkgutil
import datetime

from django.forms import Form, URLField, BooleanField, ValidationError
from models import Site, save_as_site_object
from page_tools import Page

class SiteForm(Form):
    force = BooleanField(required=False)
    url = URLField()
    
    site = None
    
    def clean_url(self):
        url = self.cleaned_data['url']
        force = self.cleaned_data['force']
        
        #Looking for the site in the database
        site_cache = Site.objects.filter(url=url)
        site_cache = site_cache.filter(date_time__gt=datetime.datetime.now()-datetime.timedelta(days=1))
        
        if force:
            site_cache = site_cache.delete()

        if site_cache:
            self.site = site_cache[0]
        else:
            try:
                home_page = Page(url)
                if home_page.status_code > 400:
                    raise ValidationError("This site does not appear to be working")
            except IOError:
                raise ValidationError("This site does not appear to be working")
        
            self.site = save_as_site_object(home_page)
            
            for platform_name in self.get_platform_names():
                signature = __import__('cmfieldguide.cmsdetector.signatures.' + platform_name, 
                    fromlist='Signature').Signature(self.site)
        
        return url
    
    def get_platform_names(self):

        names = []

        package = signatures
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
            names.append(modname)

        return names
    