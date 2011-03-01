from distutils.core import setup

setup(name='django-merchant',
      version='0.01',
      packages=['billing', 'billing.forms', 'billing.gateways.eway_gateway.eway_api', 'billing.management.commands', 'billing.models', 'billing.templatetags', 'billing.utils'],
     )
