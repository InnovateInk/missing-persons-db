"""
Django settings for missing_persons project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
import sys
from collections.abc import Callable

import environ
from django.conf import global_settings
from django.contrib.messages import constants as messages
from django.core.exceptions import ImproperlyConfigured

from ...constants.deployment import (
    ENVIRONMENT_PRODUCTION,
    ENVIRONMENT_STAGING,
    KNOWN_ENVIRONMENTS,
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR: Callable = environ.Path(__file__) - 4
# app directory path override
APPS_DIR = os.path.join(BASE_DIR, "missing_persons/apps/")
sys.path.insert(0, APPS_DIR)

# env file injection
env_file = os.path.join(BASE_DIR, ".env")
env = environ.Env()
env.read_env(env_file)

ENVIRONMENT = env.str("ENVIRONMENT", default="local").lower()
IS_PRODUCTION = ENVIRONMENT == ENVIRONMENT_PRODUCTION
IS_STAGING = ENVIRONMENT == ENVIRONMENT_STAGING
IS_LOCAL = ENVIRONMENT not in KNOWN_ENVIRONMENTS

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=True)
if DEBUG and IS_PRODUCTION:
    raise ImproperlyConfigured("Debugging enabled in Production!")

ALLOWED_HOSTS = []


# CORS settingss
CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=["http://*.127.0.0.1"],
)
CORS_ALLOWED_ORIGINS = env.list(
    "CORS_ALLOWED_ORIGINS",
    default=[
        "http://*.127.0.0.1",
    ],
)
CORS_ALLOW_CREDENTIALS = env.bool("CORS_ALLOW_CREDENTIALS", default=True)


# Application definition

# Application definition
DJANGO_APPS = [
    # custom admin theme
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.humanize",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.postgres",
]

# 3rd party libraries
THIRD_PARTY_APPS = [
    "allauth",
    "allauth.account",
    "bootstrap4",
    "bootstrap_datepicker_plus",
    "django_extensions",
    "django_filters",
    "phonenumber_field",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "simple_history",
    "widget_tweaks",
]

LOCAL_APPS = [
    "missing_persons.apps.dashboard.apps.DashboardConfig",
    "missing_persons.apps.login.apps.LoginConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "missing_persons.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "missing_persons.wsgi.application"
SITE_ID = 1

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Authentication settings
AUTH_USER_MODEL = "login.UserAccount"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard:home_page"
LOGOUT_URL = "logout"
LOGOUT_REDIRECT_URL = "login"

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGES = global_settings.LANGUAGES + [("en-us", "American English")]

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MESSAGE_TAGS = {
    messages.DEBUG: "info",
    messages.INFO: "info",
    messages.SUCCESS: "success",
    messages.WARNING: "warning",
    messages.ERROR: "error",
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
SHELL_PLUS = "ipython"
# Phone number validator
PHONENUMBER_DEFAULT_REGION = "KE"
# REST framework configuration
DEFAULT_RENDERER_CLASSES = ("rest_framework.renderers.JSONRenderer",)

if DEBUG:
    DEFAULT_RENDERER_CLASSES = DEFAULT_RENDERER_CLASSES + (
        "rest_framework.renderers.BrowsableAPIRenderer",
    )


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": DEFAULT_RENDERER_CLASSES,
    "DEFAULT_PAGINATION_CLASS": "missing_persons.common.pagination.ResultsPagination",
    "DEFAULT_VERSIONING_CLASS": "missing_persons.common.versioning.MissingPersonsURLPathVersioning",
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.ScopedRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "generic_high": "1000/day",
        "generic_low": "20/day",
    },
}

SPECTACULAR_SETTINGS = {
    "TITLE": "missing persons db API",
    "DESCRIPTION": "missing persons db API documentation",
    "VERSION": "0.1.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",  # shorthand to use the sidecar instead
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

# Email settings
DEFAULT_EMAIL_DOMAIN = env("DEFAULT_EMAIL_DOMAIN", default="@missing_persons.com")
SUPPORT_FROM_NAME = env("SUPPORT_FROM_NAME", default="missing persons db Support")
SUPPORT_FROM_EMAIL_NAME = env("SUPPORT_FROM_EMAIL_NAME", default="support")
SUPPORT_REPLY_TO_EMAIL_NAME = env("SUPPORT_REPLY_TO_EMAIL_NAME", default="support")

DEFAULT_FROM_EMAIL = SUPPORT_FROM_EMAIL_NAME + DEFAULT_EMAIL_DOMAIN
CONTACT_EMAIL_RECIPIENTS = env.list(
    "CONTACT_EMAIL_RECIPIENTS", default=[SUPPORT_REPLY_TO_EMAIL_NAME]
)

USE_SMTP = env.bool("USE_SMTP", default=False)

if IS_LOCAL:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

if USE_SMTP:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env.str("EMAIL_HOST", default="smtp.sendgrid.net")
    EMAIL_HOST_USER = env.str("EMAIL_HOST_USER", default="apikey")
    EMAIL_HOST_PASSWORD = env.str("EMAIL_HOST_PASSWORD", default="")
    EMAIL_PORT = env.int("EMAIL_PORT", default=587)
    EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)

BOOTSTRAP4 = {
    "include_jquery": True,
}

FRONTEND_HOST = env.str("FRONTEND_HOST", default="http://localhost:8000")
