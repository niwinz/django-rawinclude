=================
django-rawinclude
=================

Small module for django that gives the ease of loading templates in raw.
That is, not rendering the content.

This really is useful for embedding javascript templates with sintaxys
similar to django. It is more useful than the templatetag "ssi" because it
uses all the logic of templateloaders of django.

**NOTE1**: Not compatible with django cache loader, but in the very near future be implemented cache itself.

**NOTE2**: it is studying ways to facilitate i18n, either through javascript, either by python.

How use it?
===========

On first step, setup your own templateloaders on ``settings.py``::

    RAWINCLUDE_TEMPLATE_LOADERS = [
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ]

    INSTALLED_APPS = [
        ...
        "rawinclude",
    ]

And second step, embedd some raw-template in your standard django template::

    {% load rawinclude %}
    {% raw_include "path/rawtemplate.html" %}
