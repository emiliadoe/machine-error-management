"""
Django settings for errorManagementSystem project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Lade die .env-Datei
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g=@v3$!hzdivkx91o4s81h@#xuor9$@u4*uu*ay14dbaejpfko'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
""" 
DEBUG = False
"""

ALLOWED_HOSTS = ['machine-error-management.onrender.com', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djangoApp.apps.DjangoappConfig',
    'cloudinary_storage',
    'cloudinary',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', 
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',  # Allow localhost access
]


ROOT_URLCONF = 'errorManagementSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [BASE_DIR / "templates"], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
               # 'djangoApp.context_processor.global_data', 
            ],
        },
    },
]

WSGI_APPLICATION = 'errorManagementSystem.wsgi.application'

CSRF_TRUSTED_ORIGINS = [
    'https://machine-error-management.onrender.com',
]

CSRF_COOKIE_SECURE = True 
CSRF_USE_SESSIONS = False 


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


import dj_database_url

database_url = os.getenv('DB_DATA')
if not database_url:
    print("Warning: DATABASE_URL is not set. Using a local database as fallback.")
    database_url = 'postgres://user:password@localhost:5432/mydatabase'  

DATABASES = {
    'default': dj_database_url.config(default=database_url)
}

""" DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME':  'manage-errors',
         'USER': os.getenv('DB_USER'),
         'PASSWORD': os.getenv('DB_PASSWORD'),
         'PORT': '5432',
         'HOST': 'localhost'
     }
 } """

#DATABASES = {
#    'default': {
#  'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'de'

TIME_ZONE = 'UTC'

USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGES = (
    ('en', 'English'),
    ('es', 'Spanish'),
    ('de', 'German'),
)

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# This production code might break development mode, so we check whether we're in DEBUG mode
if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = "home" 
LOGOUT_REDIRECT_URL = "home" 
LOGOUT_REDIRECT_URL = '/'  

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.getenv('CLOUD_NAME'),
#    'API_KEY': os.getenv('API_KEY'),
#    'API_SECRET': os.getenv('CLOUD_API_SECRET'),
#}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

import cloudinary

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('CLOUD_API_SECRET')
)