"""
Django settings for DjgLeo001 project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n5!n$cl#reb6oyd0zu*tn_ff113&dn4(71-(9cl%r9zt2v2yf5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [u'med-exams.herokuapp.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
#
    'whitenoise.runserver_nostatic',    
    'django.contrib.staticfiles',
    'DjgLeoApp001.apps.Djgleoapp001Config',
    'datetimewidget',

    'graphos',
    'gdstorage',    

    'django_filters',
#    'datatableview',
    'crispy_forms',
    'django_tables2',

#    'columns',
#    'report_builder',
    
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

MIDDLEWARE_CLASSES = [
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ]

ROOT_URLCONF = 'DjgLeo001.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), os.path.join(BASE_DIR, 'DjgLeoApp001/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'DjgLeo001.processors.setforuser.defadm',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'DjgLeo001.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

# Update database configuration with $DATABASE_URL.
DATABASES = {
    'default0': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'LeoKapa+.db'),
    },
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'MedExam',
        'USER': 'postgres',
        'PASSWORD': '130368',
        'HOST': '127.0.0.1',
        'PORT': '5434',
    }
}

import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
    }
]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'el'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

FIXTURE_DIRS = ('/fixtures/',)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'medexamsgreece'
EMAIL_HOST_PASSWORD = '094057575LE@'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

#
# Google Drive Storage Settings
#
GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE = 'MedExamPDF-f593eef68e0d.json'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

import os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8'))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#STATIC_ROOT = 'static/'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    os.path.join(CURRENT_PATH, 'static'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'
