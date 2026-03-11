import os
import sys

# Add the project directory to sys.path
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, SCRIPT_DIR)

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
