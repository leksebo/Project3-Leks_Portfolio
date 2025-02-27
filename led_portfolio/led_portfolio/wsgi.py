"""
WSGI config for led_portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'led_portfolio.settings_combined')

# Initialize Django WSGI application
application = get_wsgi_application()

# Add WhiteNoise with max-age cache headers for static files
application = WhiteNoise(application, root='staticfiles/')
application.add_files('staticfiles/', prefix='static/')
