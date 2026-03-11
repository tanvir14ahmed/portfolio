import os
import sys
import traceback

# Get the directory where this file is located
path = os.path.dirname(os.path.abspath(__file__))

# Add the directory to sys.path
if path not in sys.path:
    sys.path.append(path)

# Set the environment variable for Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

def application(environ, start_response):
    try:
        from django.core.wsgi import get_wsgi_application
        _application = get_wsgi_application()
        return _application(environ, start_response)
    except Exception:
        # If the app crashes, show the error in the browser
        status = '500 Internal Server Error'
        output = traceback.format_exc().encode('utf-8')
        response_headers = [('Content-type', 'text/plain; charset=utf-8'),
                            ('Content-Length', str(len(output)))]
        start_response(status, response_headers)
        return [output]
