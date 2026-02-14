# pythonanywhere_wsgi.py
import os
import sys

# Add your project directory to the sys.path
path = '/home/YOUR_USERNAME/YOUR_REPO_NAME'  # You'll replace YOUR_USERNAME with your PythonAnywhere username
if path not in sys.path:
    sys.path.append(path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

# Then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()