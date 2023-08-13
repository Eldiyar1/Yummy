from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-euxet4bqs=$k0^z8-ls+om^@di#)u61yy_9w*l%ab4vja+9%x%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
CREATE_APPS = [
    'apps.food_space',
]

INSTALLED_LIBRARY = [
    'rest_framework',
    'jazzmin',
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = INSTALLED_LIBRARY + CREATE_APPS + DJANGO_APPS
