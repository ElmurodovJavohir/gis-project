"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY", "django-insecure-qitr6tnh2z3euo03*l7hd6$1awr01p=h9xr$i$-ktmo3r)qo-u"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", 1)

ALLOWED_HOSTS = ["*"]
# os.getenv("ALLOWED_HOSTS", "*").split(",")

# Application definition
INSTALLED_APPS = [
    "baton",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    # third party
    "corsheaders",
    "rest_framework",
    "django_filters",
    "rest_framework_simplejwt",
    "drf_spectacular",
    # "django_elasticsearch_dsl",
    # "django_elasticsearch_dsl_drf",
    "django_better_admin_arrayfield",
    "django_celery_beat",
    "import_export",
    # apps
    "gis",
    "baton.autodiscover",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "config.urls"

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
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.asgi.application"
# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.getenv("POSTGRES_DB", "crawler"),
    #     "USER": os.getenv("POSTGRES_USER", "postgres"),
    #     "PASSWORD": os.getenv("POSTGRES_PASSWORD", "admin"),
    #     "HOST": os.getenv("POSTGRES_HOST", "localhost"),
    #     "PORT": os.getenv("POSTGRES_PORT", "5432"),
    #     "ATOMIC_REQUESTS": True,
    # },
    # "postgresql": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.getenv("POSTGRES_DB", "catalog_tm"),
    #     "USER": os.getenv("POSTGRES_USER", "postgres"),
    #     "PASSWORD": os.getenv("POSTGRES_PASSWORD", "123sql_adm!@#"),
    #     "HOST": os.getenv("POSTGRES_HOST", "10.0.150.159"),
    #     "PORT": os.getenv("POSTGRES_PORT", "5432"),
    #     "ATOMIC_REQUESTS": True,
    # },
}
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


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
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ru-ru"
CSRF_TRUSTED_ORIGINS = ["https://pricing.smartbots.uz", "http://localhost:8080"]


def gettext(s):
    return s


LANGUAGES = (
    ("ru", gettext("Uzbek-latin")),
    ("kr", gettext("Uzbek-cyrillic")),
    ("ru", gettext("Russian")),
)
MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
# REQUEST LANGUAGES
REQUEST_LANGUAGES = ("ru", "ru", "kr")
DEFAULT_LANGUAGE = "ru"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# EMAIL
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_PORT = os.getenv('EMAIT_PORT')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "SIGNING_KEY": SECRET_KEY,
    "TOKEN_OBTAIN_SERIALIZER": "user.serializers.TokenObtainPairSerializer",
    "AUTH_HEADER_TYPES": ("Bearer",),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=7),
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "config.pagination.PageSizePagination",
    "PAGE_SIZE": 10,
    "DATE_FORMAT": "%Y-%m-%d",
    "DATETIME_FORMAT": "%Y-%m-%d %H:%M:%S",
    "DATE_INPUT_FORMATS": ["%d-%m-%Y", "%Y-%m-%d"],
    "DATETIME_INPUT_FORMATS": [
        "%Y-%m-%d %H:%M",
        "%d-%m-%Y %H:%M",
        "%d/%m/%Y %H:%M",
        "%m/%d/%Y, %H:%M %p",
        "iso-8601",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}
if not DEBUG:
    REST_FRAMEWORK["EXCEPTION_HANDLER"] = ("common.exception.api_exception_handler",)


# Celery
if USE_TZ:
    CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", REDIS_URL)
BROKER_URL = os.getenv("BROKER_URL", REDIS_URL)
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", REDIS_URL)
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

CORS_ALLOW_ALL_ORIGINS = (
    True  # noqa If this is used then `CORS_ALLOWED_ORIGINS` will not have any effect
)
CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:8000',
# ]
HOST = os.getenv("HOST", "http://localhost:8000")


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "velname)s %(message)s"},
    },
    "handlers": {
        "console": {"level": "INFO", "class": "logging.StreamHandler", "formatter": "simple"},
        "logstash": {
            "level": "INFO",
            "class": "logstash.TCPLogstashHandler",
            "host": "10.0.150.158",
            "port": 5044,
            "version": 1,
            "message_type": "django",  # 'type' поле для logstash сообщения.'fqdn': False,
            "tags": ["django"],  # список тег.
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["logstash"],
            "level": "INFO",
            "propagate": True,
        }
    },
}

# NEW

# ELASTICSEARCH_DSL = {
#     "default": {"hosts": os.getenv("ELASTIC_HOST", "localhost")},
# }
# # Set to False to globally disable auto-syncing.
# ELASTICSEARCH_DSL_AUTOSYNC = False
# # Set to False not force an [index refresh] with every save.
# ELASTICSEARCH_DSL_AUTO_REFRESH = False


BATON = {
    "SITE_TITLE": "Pricing ",
    "INDEX_TITLE": "Pricing",
    "SUPPORT_HREF": "https://t.me/elmurodovjavohir",
    # "COPYRIGHT": 'Copyright © 2023 <a href="https://texnomart.uz">Texnomart.uz</a>',  # noqa
    "COPYRIGHT": "",  # noqa
    "CONFIRM_UNSAVED_CHANGES": True,
    "SHOW_MULTIPART_UPLOADING": True,
    "ENABLE_IMAGES_PREVIEW": True,
    "CHANGELIST_FILTERS_IN_MODAL": True,
    "CHANGELIST_FILTERS_ALWAYS_OPEN": False,
    "CHANGELIST_FILTERS_FORM": True,
    "MENU_ALWAYS_COLLAPSED": False,
    # 'MENU_TITLE': 'Menu',
    "MESSAGES_TOASTS": False,
    # 'GRAVATAR_DEFAULT_IMG': 'retro',
    # 'SEARCH_FIELD': {
    #     'label': 'Search contents...',
    #     'url': '/search/',
    # },
}


AVTOELON_DETAIL_URL = "https://avtoelon.uz/a/show/"
