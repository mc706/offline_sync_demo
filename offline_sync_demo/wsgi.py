"""
WSGI config for offline_sync_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os, sys, site

# Tell wsgi to add the Python site-packages to its path.
site.addsitedir('~/.virtualenvs/offline/lib/python2.7/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "offline_sync_demo.settings")

#activate_this = os.path.expanduser("~/.virtualenvs/offline/bin/activate_this.py")
#execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
workspace = os.path.abspath(os.path.dirname(__name__))
sys.path.append(workspace)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
