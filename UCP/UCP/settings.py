"""
Django settings for UCP project.

Generated by 'django-admin startproject' using Django 1.8.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.core.urlresolvers import reverse_lazy


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')lz=44u4y0t_x5$)4wler39+=@58z8%zqx&1y%lc**da*0!gtu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'login',
    'discussion',
    'news_event',
    'result',
    'schedule',
    'corsheaders',
    'rest_framework',
    'nested_admin',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'rest_framework_swagger',
    'django.contrib.auth',
    'rest_framework.authtoken',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'constance',
    'tinymce',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'UCP.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    '127.0.0.1:2000',
    'pranavtiwari.xyz',
    'gsoc.pranavtiwari.xyz',
]
CORS_ALLOW_METHODS = (
    'GET',
    'POST',
    'PUT',
    'PATCH',
    'DELETE',
    'OPTIONS'
)
CORS_ORIGIN_REGEX_WHITELIST = ('^(http?://)?([\w-]+\.)?pranavtiwari\.xyz\/?(\/[.\w]*)*',)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django_settings_export.settings_export',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'UCP.wsgi.application'

SETTINGS_EXPORT = [
    'SITE_TITLE',
    'LOGO',
    'THEME',
]
#constance
CONSTANCE_CONFIG = {
    'THE_ANSWER': (42, 'Answer to the Ultimate Question of Life, '
                       'The Universe, and Everything'),
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Rest Framework authentication

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    )
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static")


STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = '/media/'



#Page size for pagination
PAGE_SIZE = 10

#Setting up login and logout URLS
LOGIN_URL = reverse_lazy('login')

#default local settings constants
VERIFICATION_EMAIL_EXPIRY_TIME = 1

PASSWORD_RESET_CODE_EXPIRY_TIME = 1

BASE_URL = 'localhost:8000'

SITE_TITLE = "University"

LOGO = "images/logo.png"

#Theme for the site
"""
Choices - 
    paper
    cerulean
    journal
    flat
    readable
"""

THEME = "journal"

#import local_settings.py file if it exists
try:
    from settings_local import *
except ImportError:
    print "please create a local settings file"
    pass


