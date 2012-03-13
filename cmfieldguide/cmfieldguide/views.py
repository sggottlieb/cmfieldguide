import engine
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import    HttpResponse

def home(request):

    url = ''
    results = None

    if request.GET.has_key('u'):
        url = request.GET['u']
        results = engine.test(url)


    c = {
        'url': url,
        'results': results
    }

    return render_to_response('cmfieldguide/templates/results.html', c, context_instance=RequestContext(request))