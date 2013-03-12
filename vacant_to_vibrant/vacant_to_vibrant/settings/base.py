import os
from os.path import abspath, dirname

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
        raise ImproperlyConfigured(error_msg)

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # > createdb -T template_postgis philly_living_lots
        # > psql
        # # create user philly_living_lots with password 'password';
        # # grant all privileges on database philly_living_lots to
        # philly_living_lots;
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': get_env_variable('PHILLY_LIVING_LOTS_DB_NAME'),
        'USER': get_env_variable('PHILLY_LIVING_LOTS_DB_USER'),
        'PASSWORD': get_env_variable('PHILLY_LIVING_LOTS_DB_PASSWORD'),
        'HOST': get_env_variable('PHILLY_LIVING_LOTS_DB_HOST'),
        'PORT': get_env_variable('PHILLY_LIVING_LOTS_DB_PORT'),
    }
}

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

PROJECT_ROOT = os.path.join(abspath(dirname(__file__)), '..', '..')

DATA_ROOT = os.path.join(PROJECT_ROOT, 'data')

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

SECRET_KEY = get_env_variable('GROWING_CITIES_SECRET_KEY')

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'fiber.middleware.ObfuscateEmailAddressMiddleware',
    'fiber.middleware.AdminPageMiddleware',

    'reversion.middleware.RevisionMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

ROOT_URLCONF = 'vacant_to_vibrant.urls'

WSGI_APPLICATION = 'vacant_to_vibrant.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (

    #
    # django contrib
    #
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.gis',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    #
    # third-party
    #
    'actstream',
    'compressor',
    'contact_form',
    'fiber',
    'mptt',
    'reversion',
    'reversion_compare',
    'south',

    #
    # first-party
    #
    'activity_stream',
    'contact',
    'lots',
    'organize',
    'phillydata',
    'phillydata.availableproperties',
    'phillydata.landuse',
    'phillydata.opa',
    'phillydata.owners',
    'phillydata.parcels',
    'phillydata.taxaccounts',
    'phillydata.violations',
    'phillydata.waterdept',
    'places',
    'sync',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

PLACES_CLOUDMADE_KEY = '781b27aa166a49e1a398cd9b38a81cdf'
PLACES_CLOUDMADE_STYLE = '82682'

FIBER_TEMPLATE_CHOICES = (
    ('base.html', 'Default template'),
)

SOUTH_TESTS_MIGRATE = False