from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

class SitedownMiddleware(object):
    """
    Site down middleware. If enabled, each Django-powered URL will
    redirect to a message, except for admin.
    
    """
    def __init__(self):
        self.template = getattr(settings, 'SITEDOWN_TEMPLATE', 'sitedown/default.html' )
    
    def process_request(self, request):
        if getattr(settings, 'SITEDOWN_DISABLE', False):
            return None
        if request.path.startswith('/admin'):
            return None
        return render_to_response(self.template,
            RequestContext( request, {}))
        
