import engine
from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext
from forms import SiteForm



def index(request):
    
    url = ''
    site = None
    
    if 'url' in request.GET:
        form = SiteForm(data=request.GET)
        if form.is_valid():
            site = engine.test(form.cleaned_data['url'], 'force' in request.GET)
    else:
        form = SiteForm()
    
    return render_to_response('index.html', 
        {'form':form,
         'site':site,
         'media_root': settings.STATIC_ROOT
        },
        context_instance=RequestContext(request))