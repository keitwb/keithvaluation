# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1

SECRET_KEY = os.environ.get("SECRET_KEY", "!916gumezvl!m@g)r9jd%(6o#2f(bnk6v$&olh&x_+6q72mrj5")

DEBUG = os.environ.get("DJANGO_DEBUG") == "y"

SERVER_HOSTNAME = os.environ.get("SITE_HOSTNAME")
ALLOWED_HOSTS = ["localhost", "www.%s" % SERVER_HOSTNAME, SERVER_HOSTNAME]


# Application definition

INSTALLED_APPS = (
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "django_extensions",
    "keithvaluation",
)

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": (
                "django.core.context_processors.media",
                "keithvaluation.context_processors.google_keys",
                "keithvaluation.context_processors.feature_flags",
            ),
            "loaders": ["django.template.loaders.app_directories.Loader"],
        },
    }
]

ROOT_URLCONF = "keithvaluation.urls"

WSGI_APPLICATION = "keithvaluation.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "/data/sqlite/keithvaluation.db"}}

if DEBUG:
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.memcached.PyLibMCCache",
            "LOCATION": "memcached:11211",
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATIC_ROOT = "/build/dist/"
STATIC_URL = "//%s%s" % (
    os.environ.get("DJANGO_STATIC_HOSTNAME", SERVER_HOSTNAME),
    os.environ.get("DJANGO_STATIC_PATH", "/static/"),
)

MEDIA_ROOT = "/media/"
MEDIA_URL = STATIC_URL + "media/"

GA_ACCOUNT = os.environ.get("DJANGO_GA_ACCOUNT", None)
GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", None)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"simple": {"format": "%(levelname)s %(message)s"}},
    "filters": {},
    "handlers": {"console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "simple"}},
    "loggers": {
        "django.request": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
        "": {"handlers": ["console"], "level": "DEBUG", "propagate": False},
    },
}

if os.environ.get("DJANGO_ADMIN") in ["y", "yes", "t", "true", "1"]:
    from .admin import *
