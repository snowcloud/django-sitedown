from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect

class SitedownMiddleware(object):
    """
    Site down middleware. If enabled, each Django-powered URL will
    redirect to a message, except for admin.
    
    """
    def __init__(self):
        self.template_path = getattr(settings, 'SITEDOWN_TEMPLATE', '/sitedown/default.html' )
    
    def process_request(self, request):
        if getattr(settings, 'DISABLE_SITEDOWN', False):
            return None
        if request.path.startswith('/admin'):
            return None
            # if request.POST:
            #     return login(request)
            # else:
            #     return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))
        return None
        
    # def allowed_path(self, requested_path):
    #     for p in settings.AUTH_ALLOWED_PATHS:
    #         if requested_path.startswith(p):
    #             print p
    #             return True
    #     path = requested_path.split('/')[1]
    #     if path in settings.AUTH_ALLOWED_PATHS:
    #         return True
    #     return requested_path == self.require_login_path
