import os
import sys
import traceback

# Add the project directory to sys.path
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, SCRIPT_DIR)

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

def application(environ, start_response):
    try:
        from django.core.wsgi import get_wsgi_application
        _application = get_wsgi_application()
        return _application(environ, start_response)
    except Exception:
        # If the app fails to start, show the error in the browser
        error_msg = traceback.format_exc()
        status = '500 Internal Server Error'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return [f"CRITICAL ERROR DURING STARTUP:\n\n{error_msg}".encode('utf-8')]
