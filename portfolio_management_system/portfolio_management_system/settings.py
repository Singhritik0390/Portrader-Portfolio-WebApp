"""
Django settings for portfolio_management_system project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Reference: https://dev.to/vladyslavnua/how-to-protect-your-django-secret-and-oauth-keys-53fl 
# For handling the environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Our Apps
    'home',
    'dashboard',
    'riskprofile',

    # Third Party - 1) All Auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.twitter',
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

ROOT_URLCONF = 'portfolio_management_system.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # `allauth` needs this from django
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'portfolio_management_system.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Required for all-auth
SITE_ID = 1


# Provider specific settings for all-auth apps
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': str(os.getenv('FACEBOOK_CLIENT_ID')),
            'secret': str(os.getenv('FACEBOOK_SECRET_KEY')),
            'key': ''
        }
    },
    'google': {
        'APP': {
            'client_id': str(os.getenv('GOOGLE_CLIENT_ID')),
            'secret': str(os.getenv('GOOGLE_SECRET_KEY')),
            'key': ''
        }
    },
    'twitter': {
        'APP': {
            'client_id': str(os.getenv('TWITTER_CLIENT_ID')),
            'secret': str(os.getenv('TWITTER_SECRET_KEY')),
            'key': ''
        }
    }
}

# Email Backend - Currently set at console/terminal
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Custom Settings - allauth
LOGIN_REDIRECT_URL = "/"

# Alphavantage key
ALPHAVANTAGE_KEY1 = str(os.getenv('SI8A85AINB8BGB3P'))
ALPHAVANTAGE_KEY2 = str(os.getenv('GYEWDGN84PISC8I0'))
ALPHAVANTAGE_KEY3 = str(os.getenv('GYEWDGN84PISC8I0'))
ALPHAVANTAGE_KEY4 = str(os.getenv('GYEWDGN84PISC8I0'))
ALPHAVANTAGE_KEY5 = str(os.getenv('GYEWDGN84PISC8I0'))
ALPHAVANTAGE_KEY6 = str(os.getenv('GYEWDGN84PISC8I0'))
ALPHAVANTAGE_KEY7 = str(os.getenv('GYEWDGN84PISC8I0'))

NEWSAPI_KEY = "419c267c28264e4da11e0408225b9ed9"
ALPHAVANTAGE_KEY1 = "SI8A85AINB8BGB3P"