from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.template import RequestContext

from forms import SiteForm
from models import PlatformSiteTest


@login_required
def index(request):
    
    url = ''
    site = None
    
    if 'url' in request.GET:
        form = SiteForm(data=request.GET)
        if form.is_valid():
            site = form.site
    else:
        form = SiteForm()
    
    return render_to_response('index.html', 
        {'form':form,
         'site':site,
         'media_root': settings.STATIC_ROOT,
         'next': request.get_full_path().rstrip('&force=on')
        },
        context_instance=RequestContext(request))
        
@login_required
@require_POST
def platform_reject(request, id):
    site_test = get_object_or_404(PlatformSiteTest, pk=int(id))
    site_test.visitor_rejects = not site_test.visitor_rejects
    site_test.save()
    return HttpResponseRedirect(request.POST['next'])
    
