from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

import urlparse

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
        # print settings.STATIC_PATH
        return render_to_response(self.template,
            RequestContext( request, {}))
        
