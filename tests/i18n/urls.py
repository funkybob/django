from __future__ import unicode_literals

from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponse, StreamingHttpResponse
from django.test import ignore_warnings
from django.utils.deprecation import RemovedInDjango20Warning
from django.utils.translation import gettext_lazy as _

# test deprecated version of i18n_patterns() function (with prefix). Remove it
# and convert to list of urls() in Django 2.0
i18n_patterns = ignore_warnings(category=RemovedInDjango20Warning)(i18n_patterns)

urlpatterns = i18n_patterns('',
    (r'^simple/$', lambda r: HttpResponse()),
    (r'^streaming/$', lambda r: StreamingHttpResponse([_("Yes"), "/", _("No")])),
)
