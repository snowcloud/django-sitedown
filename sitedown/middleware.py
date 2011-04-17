from django.conf import settings
from django.contrib.auth.views import login
from django.contrib.flatpages.models import FlatPage
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
        self.disabled = getattr(settings, 'SITEDOWN_DISABLE', False)
        self.static_url = getattr(settings, 'STATIC_URL', False)
        self.redirect = getattr(settings, 'SITEDOWN_REDIRECT', '/sitedown/')
        self.use_302 = getattr(settings, 'SITEDOWN_USE_302', False)
        self.flatpage = getattr(settings, 'SITEDOWN_FLATPAGE', False)
        
    def process_request(self, request):
        if  self.disabled or \
            request.path.startswith('/admin') or \
            request.path.startswith(urlparse.urlparse(settings.MEDIA_URL).path) or \
            (self.static_url and request.path.startswith(urlparse.urlparse(settings.STATIC_URL))):
            return None
        if request.path == self.redirect:
            return render_to_response(self.template,
                RequestContext( request, {}))
        if self.use_302:
            return HttpResponseRedirect(self.redirect)
        else:
            response = HttpResponseServiceUnavailable(mimetype='text/html')
            t = loader.get_template(self.template)
            if self.flatpage:
                fp = FlatPage.objects.get(url=self.flatpage)
                title = fp.title
                message = fp.content
            else:
                title = message = ''
            response.write(t.render(RequestContext( request, { 'title': title, 'message': message })))
            return response
        
