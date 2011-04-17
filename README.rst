================
 Django Sitedown
================

Django-Sitedown is a simple app to effectively take a site off-line. Any URL except /admin will be redirected to a holding page.

Install Django-Sitedown somewhere Django will find it.

Configure settings.py:

Add 'sitedown' to INSTALLED_APPS
Add this to MIDDLEWARE_CLASSES:
"sitedown.middleware.SitedownMiddleware",

Set SITEDOWN_TEMPLATE, default is 'sitedown/default.html'.
Set SITEDOWN_DISABLE to True to disable, default is False.
