"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.0.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import django_heroku
import os
from decouple import config, Csv



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)



INSTALLED_APPS = [
    # own
    'user',
    'qanda',
    'contact',
    # 3rd party
    'markdownify',
    'crispy_forms',
    'social_django',

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
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# static files settings
STATIC_URL = '/static/'
# location where you will store your static files like bootstrap
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
]
# location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MARKDOWNIFY_STRIP = False
MARKDOWNIFY_WHITELIST_TAGS = [
    'a','blockquaote', 'h7', 'h6', 'h4', 'h5', 'h3', 'h2', 'h1', 'code',
    'em', 'li', 'ol', 'p', 'strong', 'ul',
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_URL = 'user:login'
LOGIN_REDIRECT_URL = 'questions:index'
LOGOUT_REDIRECT_URL = 'questions:index'

ES_INDEX = 'answerly'
ES_HOST = 'localhost'
ES_PORT = '9200'

CHROMEDRIVER =os.path.join(BASE_DIR, '../chromedriver')  #tests

EMAIL_BACKEND = config('E_BACK')
EMAIL_HOST = config('E_HOST')
EMAIL_HOST_USER = config('E_HOST_USER')
EMAIL_HOST_PASSWORD = config('E_PASS')
EMAIL_PORT = config('E_PORT', cast=int)
EMAIL_USE_TLS = config('E_TLS')

SOCIAL_AUTH_GITHUB_KEY = config('GIT_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('HUB_KEY')

#Activation heroku
django_heroku.settings(locals())