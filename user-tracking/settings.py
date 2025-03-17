from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY: Keep the secret key safe in production
SECRET_KEY = 'django-insecure-=y$k2so+-bd2mh2ss8at$*xaf@06_^dz3f5&m)mnvz*u=n^mxd'

# SECURITY: Disable debug in production
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'trip',
    'rest_framework',
    'django.contrib.staticfiles',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]

ROOT_URLCONF = 'user-tracking.urls'
CORS_ALLOW_ALL_ORIGINS = True 

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

WSGI_APPLICATION = 'user-tracking.wsgi.application'


# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'railway',
        'USER': 'postgres',
        'PASSWORD': 'TIWcbTvBhcIqPdQeAurNKsvmhgOmwySm',
        'HOST':'shinkansen.proxy.rlwy.net',
        'PORT': '26665',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
USE_L10N = True

# Static & Media Files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
