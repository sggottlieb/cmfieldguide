from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

def detector_forward(request):
    return HttpResponseRedirect(reverse('detector_index'))
    
