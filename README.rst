================
 Django Sitedown
================

Django-Sitedown is a simple app to effectively take a site off-line. Any URL except /admin will be redirected to a holding page.

This is just a convenience thing for when you're making changes and just want to switch off a Django project for a short while. You are probably better off doing this via a redirect in your web server to a 503 Service Unavailable. 


To use it, install Django-Sitedown somewhere Django will find it.

Configure settings.py:

Add 'sitedown' to INSTALLED_APPS
Add this to MIDDLEWARE_CLASSES:
"sitedown.middleware.SitedownMiddleware",

Set SITEDOWN_TEMPLATE, default is 'sitedown/default.html'.
Set SITEDOWN_DISABLE to True to disable, default is False.
Set SITEDOWN_USE_302 to True to return HTTP code 302, default is False.
Set SITEDOWN_FLATPAGE to the URL of a Flatpage to include that in the template as {{title}} and {{message}}.

Default is to return a 503 Service Unavailable

"The server is currently unable to handle the request due to a temporary overloading or maintenance of the server."
http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html

