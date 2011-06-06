from django.conf import settings

SHORT_CODE = getattr(settings, 'MOBILE_SHORT_CODE')
BACKEND = getattr(settings, 'MOBILE_BACKEND')
DEFAULT_INTERNATIONAL_PREFIX = getattr(settings, 'MOBILE_DEFAULT_INTERNATIONAL_PREFIX')

try:
    GATE_USERNAME = getattr(settings, 'GATE_USERNAME')
    GATE_PASSWORD = getattr(settings, 'GATE_PASSWORD')
except AttributeError:
    pass