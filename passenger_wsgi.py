import os
import sys
import subprocess

# Add the project directory to sys.path
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, SCRIPT_DIR)

# --- AUTO-SETUP BLOCK (Runs on every app restart) ---
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

def run_setup():
    try:
        # 1. Run Migrations
        subprocess.run([sys.executable, 'manage.py', 'migrate', '--noinput'], check=True)
        # 2. Collect Static
        subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'], check=True)
        # 3. Create a log file to confirm it ran
        with open('setup_done.log', 'a') as f:
            from datetime import datetime
            f.write(f"Setup ran successfully at {datetime.now()}\n")
    except Exception as e:
        with open('setup_error.log', 'a') as f:
            f.write(f"Setup failed: {str(e)}\n")

# Run the setup
run_setup()
# ---------------------------------------------------

# Import the Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
