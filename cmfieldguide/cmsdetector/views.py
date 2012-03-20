import engine
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import SiteForm

def index(request):

    url = ''
    platforms = []
    if 'url' in request.GET:
        form = SiteForm(data=request.GET)
        if form.is_valid():
            platforms = engine.test(form.cleaned_data['url'])
            
    else:
        form = SiteForm()
    
    return render_to_response('index.html', 
        {'form':form,
         'platforms':platforms
        },
        context_instance=RequestContext(request))