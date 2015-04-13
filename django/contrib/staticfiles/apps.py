from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StaticFilesConfig(AppConfig):
    name = 'django.contrib.staticfiles'
    verbose_name = _("Static Files")
