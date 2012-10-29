from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module
from django.conf import settings


def get_backend(path):
    """Return a backend."""
    module_name, klass_name = path.rsplit('.', 1)

    try:
        module = import_module(module_name)
    except ImportError, e:
        raise ImproperlyConfigured('Error importing SMS backend %s: %s' % (module_name, e))

    try:
        klass = getattr(module, klass_name)
    except AttributeError:
        raise ImproperlyConfigured('Module %s does not define a %s class' % (module_name, klass_name))

    return klass

backend = get_backend(settings.MOBILE_BACKEND)
