from pathlib import Path

#################
# CORE SETTINGS #
#################

DEBUG = True
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = "django-insecure-_=+%lcowvd+4jy%gpgj9-%cyzoke3_dnl0c&+_3hkwnzg+*m)h"
WSGI_APPLICATION = "pennywise.wsgi.application"
ROOT_URLCONF = "pennywise.urls"
ALLOWED_HOSTS = []


################
# APPLICATIONS #
################

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_htmx",
    "authentication",
]


##############
# MIDDLEWARE #
##############

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
]


#############
# TEMPLATES #
#############

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


#############
# DATABASES #
#############

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


##################
# AUTHENTICATION #
##################

AUTH_USER_MODEL = "authentication.AppUser"

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

LOGIN_URL = "/authentication/sign-in"


########################
# INTERNATIONALIZATION #
########################

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


################
# STATIC FILES #
################

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


#################
# MISC SETTINGS #
#################

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
