# app/settings_production.py
from .settings import *
import dj_database_url
from decouple import config

# Security settings
DEBUG = False
SECRET_KEY = config('SECRET_KEY', default='django-insecure-)&9#4abl8vx12l7%+7a7#suk8(h5@#7hwkv^*e5+y^f()bnb^(')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1,.pythonanywhere.com,.onrender.com,.vercel.app').split(',') # type: ignore

# Database - use environment variable
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL', default='sqlite:///db.sqlite3'), # type: ignore
        conn_max_age=600
    )
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Security settings for production
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True