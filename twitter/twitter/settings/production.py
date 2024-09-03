from .base import *

DEBUG = True

ALLOWED_HOSTS = [
    'twitter-65el8x4yj-daniloalrs-projects.vercel.app',
    'twitter-daniloalr-daniloalrs-projects.vercel.app',
    '127.0.0.1'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
