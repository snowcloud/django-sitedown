from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

import urlparse

class HttpResponseServiceUnavailable(HttpResponse):
    status_code = 503
    
class SitedownMiddleware(object):
    """
    Site down middleware. If enabled, each Django-powered URL will
    redirect to a message, except for admin.
    
    """
    def __init__(self):
        self.template = getattr(settings, 'SITEDOWN_TEMPLATE', 'sitedown/default.html' )
    
    def process_request(self, request):
        if  getattr(settings, 'SITEDOWN_DISABLE', False) or \
            request.path.startswith('/admin') or \
            request.path.startswith(urlparse.urlparse(settings.MEDIA_URL).path) or \
            (getattr(settings, 'STATIC_URL', False) and request.path.startswith(urlparse.urlparse(settings.STATIC_URL))):
            return None
        if request.path == getattr(settings, 'SITEDOWN_REDIRECT', '/sitedown/'):
            return render_to_response(self.template,
                RequestContext( request, {}))
        if getattr(settings, 'SITEDOWN_USE_302', False):
            return HttpResponseRedirect(getattr(settings, 'SITEDOWN_REDIRECT', '/sitedown/'))
            
        # return a 503
        response = HttpResponseServiceUnavailable(mimetype='text/html')
        t = loader.get_template(self.template)
        response.write(t.render(RequestContext( request, {})))
        return response
        
