import os
import sys

# DEBUG: Ensure we are in the right directory
path = os.path.dirname(os.path.abspath(__file__))
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

def application(environ, start_response):
    try:
        from django.core.wsgi import get_wsgi_application
        _application = get_wsgi_application()
        return _application(environ, start_response)
    except Exception as e:
        import traceback
        status = '500 Internal Server Error'
        errors = [
            b"CRITICAL ERROR IN PASSENGER_WSGI.PY",
            b"-" * 40,
            f"Error: {str(e)}".encode('utf-8'),
            b"\nFull Traceback:\n",
            traceback.format_exc().encode('utf-8')
        ]
        response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(sum(len(x) for x in errors)))]
        start_response(status, response_headers)
        return errors
