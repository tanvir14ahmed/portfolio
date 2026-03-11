import os
import sys

# Get the project path
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

# Ensure the environment sees the project and apps
sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
