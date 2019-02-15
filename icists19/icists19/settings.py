"""
Django settings for icists19 project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-_nl)!1ln0-to4*6&bf6mdti+id71@g97c(x67clw1gy8ciup$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '54.180.8.50',
    'ec2-54-180-8-50.ap-northeast-2.compute.amazonaws.com', 
]


# Application definition

# We need to tell this project that an app is installed!
# python manage.py makemigrations <app-name>
# By running makemigrations, you're telling Django that you've made some changes to your models.

INSTALLED_APPS = [
    'front.apps.FrontConfig',
    'participant_manager.apps.ParticipantManagerConfig',
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# This config makes the root url direct to the icists19/urls.py (There is a urlpatterns -- list)
# And Django will transverse the patterns in order.
ROOT_URLCONF = 'icists19.urls'


# Project's Templates Setting describes how Djnago will laod and render templates.
# The default settings file configures a DjnagoTemplates backend whose APP_DIRS option is set to True.
# By Convention DjangoTemplates looks for a templates subdirectory in each of the INSTALLED APPS.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'icists19.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# By default, django uses SQLite.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_FRONT_DIR = os.path.join(BASE_DIR, 'front/static')
STATICFILES_DIRS = [
#    STATIC_DIR,
    STATIC_FRONT_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
