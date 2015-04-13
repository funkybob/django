# Wrapper for loading templates from eggs via pkg_resources.resource_string.
from __future__ import unicode_literals

from django.apps import apps
from django.template.base import TemplateDoesNotExist

from .base import Loader as BaseLoader

try:
    from pkg_resources import resource_string
except ImportError:
    resource_string = None


class Loader(BaseLoader):

    def __init__(self, engine):
        if resource_string is None:
            raise RuntimeError("Setuptools must be installed to use the egg loader")
        super(Loader, self).__init__(engine)

    def load_template_source(self, template_name, template_dirs=None):
        """
        Loads templates from Python eggs via pkg_resource.resource_string.

        For every installed app, it tries to get the resource (app, template_name).
        """
        pkg_name = 'templates/' + template_name
        for app_config in apps.get_app_configs():
            try:
                resource = resource_string(app_config.name, pkg_name)
            except Exception:
                continue
            return (resource, 'egg:%s:%s' % (app_config.name, pkg_name))
        raise TemplateDoesNotExist(template_name)
