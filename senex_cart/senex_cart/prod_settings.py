from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG
THUMBNAIL_DEBUG = DEBUG

ADMINS = (
    ('Michael Anderson', 'michael@senexcycles.com'),
)

MANAGERS = ADMINS

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '!e7=(lo95id2%tkk6o8qtz7b4np!5_3ed&v%i(u=dv+l^h_wfg')

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.senexcycles.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'contact@senexcycles.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = 'contact@senexcycles.com'
SERVER_EMAIL = 'contact@senexcycles.com'
########## END EMAIL CONFIGURATION

# Database
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD', '')
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "senex_cart",
        "USER": "senex_cart",
        "PASSWORD": DATABASE_PASSWORD,
        "HOST": "localhost",
        "PORT": "",
        }
}

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
########## END CACHE CONFIGURATION

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

########## ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    '.senexcycles.com',
    '127.0.0.1',
]
########## END ALLOWED HOSTS CONFIGURATION

########## SSL CONFIGURATION
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
########## END SSL CONFIGURATION

########## STRIPE CONFIGURATION
# See: http://django-stripe-payments.readthedocs.org/en/latest/installation.html
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY', 'pk_test_BnKaAmgD81hWGi1F1suzPmX6')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_x1CjT9YMoj30rlpg50CnmD8A')
########## END STRIPE

########## NEW RELIC CONFIGURATION
# See:
NEW_RELIC = True
########## END NEW RELIC CONFIGURATION

