import os
import sys

# Get the directory where this file is located
path = os.path.dirname(os.path.abspath(__file__))

# Add the directory to sys.path
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Import the standard Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
