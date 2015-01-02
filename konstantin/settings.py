"""
Django settings for konstantin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, hashlib
from fnmatch import fnmatch
from varlet import variable

from django.core.urlresolvers import reverse_lazy
from django.contrib.messages import constants as messages
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP, LOGGING, AUTHENTICATION_BACKENDS

try:
	import pymysql
	pymysql.install_as_MySQLdb()
except ImportError as e:
	pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

here = lambda *path: os.path.normpath(os.path.join(os.path.dirname(__file__), *path))
ROOT = lambda *path: here("../", *path)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'bootstrap3_datetime',
    'celery',
    'coverage',
    'model_mommy',
    'konstantin.home',
    'konstantin.files',
    'konstantin.utils',
    'konstantin.utils.templatetags.sickform',
    'konstantin.stuff',
)

MIDDLEWARE_CLASSES = (
        #'konstantin.middleware.ArduinoMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )


ROOT_URLCONF = 'konstantin.urls'

WSGI_APPLICATION = 'konstantin.wsgi.application'

PHANTOMJS_BINARY = ROOT('konstantin/static/bin/phantomjs')
CAPTURE_SCRIPT_PATH = ROOT('konstantin/static/bin/capture.js')

BROKER_URL = variable("BROKER_URL", 'amqp://guest:guest@localhost:5672')
CELERY_ACKS_LATE = True
CELERY_RESULTS_BACKEND = 'amqp'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = ROOT("static")

STATICFILES_DIRS = (
	# Put strings here, like "/home/html/static" or "C:/www/django/static".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	here("static"),

)

MEDIA_URL = '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"

MEDIA_ROOT = ROOT("media")

TMP_ROOT = ROOT("tmp")

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
)

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
	here("templates"),
	here("utils/templates"),
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = True
#ALLOWED_HOSTS = ALLOWED_HOSTS + [".nip.io"]
#HOSTNAME = "10.0.0.10.nip.io:8000" # remember you got rid of the nip.io thing
#SESSION_COOKIE_DOMAIN = '.nip.io'
ADMINS = (
# ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': variable('ENGINE',default='django.db.backends.mysql'), # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': variable('NAME',default=''), # Or path to database file if using sqlite3.
        'USER': variable('USER',default='root'),
        'PASSWORD': variable('PASSWORD',default=''),
        'HOST': variable('HOST',default='localhost'), # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': variable('PORT',default=''), # Set to empty string for default.
    },
}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = variable('SECRET_KEY', default=hashlib.sha1(os.urandom(64)).hexdigest())
