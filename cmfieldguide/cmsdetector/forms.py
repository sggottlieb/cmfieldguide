import urllib2
from django.forms import Form, URLField, ValidationError

class SiteForm(Form):
    url = URLField()
    
    def clean_url(self):
        url = self.cleaned_data['url']
        
        try:
            response = urllib2.urlopen(url)
        except IOError:
            raise ValidationError("This site does not appear to be working")
        
        if response.getcode() not in (200,):
            raise ValidationError("This site does not appear to be working")

        return url