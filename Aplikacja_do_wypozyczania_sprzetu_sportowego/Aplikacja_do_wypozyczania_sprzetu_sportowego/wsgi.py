"""
WSGI config for Aplikacja_do_wypozyczania_sprzetu_sportowego project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aplikacja_do_wypozyczania_sprzetu_sportowego.settings')

application = get_wsgi_application()
