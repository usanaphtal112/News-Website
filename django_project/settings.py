"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 4.0.10.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path


from environs import Env  # new

env = Env()  # new
env.read_env()  # new

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True  # For local server only
DEBUG = env.bool("DEBUG", default=False)  # During deployment it must e false

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",  # new
    "django.contrib.staticfiles",
    # 3rd Party
    "crispy_forms",  # new
    "crispy_bootstrap5",  # new
    "corsheaders",  # New
    # Local apps
    "accounts.apps.AccountsConfig",
    "pages.apps.PagesConfig",
    "articles.apps.ArticlesConfig",  # new
]

TIME_ZONE = "Asia/Kolkata"  # new

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django_session_timeout.middleware.SessionTimeoutMiddleware",  # new
    "corsheaders.middleware.CorsMiddleware",  # New
    "whitenoise.middleware.WhiteNoiseMiddleware",  # new
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOWED_ORIGINS = [
    "https://news-website-production-5b6e.up.railway.app",
    "https://*.railway.app",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]

CSRF_TRUSTED_ORIGINS = ["https://news-website-production-de08.up.railway.app"]

SESSION_EXPIRE_SECONDS = 60  # 1 hour
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD = 1  # group by minute
SESSION_TIMEOUT_REDIRECT = "login"

ROOT_URLCONF = "django_project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "django_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

# DATABASES = {
#     "default": {
#         #'ENGINE': 'django.db.backends.sqlite3',
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "railway",
#         "USER": "postgres",
#         "PASSWORD": "DA0dVATzKeNKfmIYrQt7",
#         "HOST": "containers-us-west-104.railway.app",
#         "PORT": "5837",
#     }
# }

DATABASES = {"default": env.dj_db_url("DATABASE_URL")}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # new
STATIC_ROOT = BASE_DIR / "staticfiles"  # new
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  # new


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.CustomUser"  # new

LOGIN_REDIRECT_URL = "home"  # new
LOGOUT_REDIRECT_URL = "home"  # new

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # new
CRISPY_TEMPLATE_PACK = "bootstrap5"  # new

# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # new

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # new

# Sendinblue

DEFAULT_FROM_EMAIL = "naphtaldanny@gmail.com"
EMAIL_HOST = "smtp-relay.sendinblue.com"
EMAIL_HOST_USER = "naphtaldanny@gmail.com"
EMAIL_HOST_PASSWORD = "pxfbsqnGKtJEBgUM"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Send Grid

# DEFAULT_FROM_EMAIL = "naphtaldanny@gmail.com"
# EMAIL_HOST = "smtp.sendgrid.net"
# EMAIL_HOST_USER = "apikey"
# EMAIL_HOST_PASSWORD = (
#     "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"
# )
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
