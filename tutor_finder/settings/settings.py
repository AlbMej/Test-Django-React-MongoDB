"""
Django settings for tutor_finder project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/

Description

This file sets global level variables for the Tutor Finder Web app
"""
import os
from decouple import config
import dj_database_url

""" BASE SETTINGS """

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

####################################################################
# SECURITY WARNING: keep the secret key used in production secret! #### Moved secret keys to environment variable ####
####################################################################

# SECRET_KEY = os.environ['SECRET_KEY']  #<-- Use this if you store your secret keys as an environment variable (EX. export SECRET_KEY="mYsEcReTkEy")
SECRET_KEY = config('SECRET_KEY')
###################################################################
# SECURITY WARNING: don't run with debug turned on in production! #### People kept committing local credentials file by accident ####
###################################################################
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.1.179','192.16=8.1.179']
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Application definition

INSTALLED_APPS = [
    'channels',
    'channels_presence',
    'tutor_finder.core',
    'tutor_finder',
    'django.contrib.admin',     # Uncomment line to enable the admin:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrap4',
    'crispy_forms',
    'chat',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'tutor_finder.urls'

TEMPLATES = [{
    'BACKEND' : 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\','/')],
    'APP_DIRS': True,
    'OPTIONS' : {
        'context_processors': ['django.template.context_processors.debug', 'django.template.context_processors.request', 'django.contrib.auth.context_processors.auth',
                               'django.contrib.messages.context_processors.messages', ],
    },
}, ]

WSGI_APPLICATION = 'tutor_finder.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

###################################################################
#          Moved database credentials to a local file             #
###################################################################



DATABASES = {}
# DATABASES['default'] = dj_database_url.config(default='sqlite:/mydatabase.sqlite') # Fall back to sqlite, can create database when running migrations
DATABASES['default'] = dj_database_url.config(default='postgres://postgres@localhost/test_db') # Need to have Postgres installed locally and test_db set up.

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
}, {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
}, ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication',],
    'DEFAULT_PERMISSION_CLASSES'    : ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly']
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tutor.finder.team@gmail.com'
EMAIL_HOST_PASSWORD = 'uyjgdjsfkipajvip'

#DEFAULT_FROM_EMAIL = 'donotreply@tutorfinder.com'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


# Channels
ASGI_APPLICATION = 'tutor_finder.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
