from .base import *  # noqa

# from django.contrib.messages import constants as messages

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Media

# MEDIA_URL = "media/"

# MEDIA_ROOT = BASE_DIR / "media"  # noqa

# Redirects

LOGIN_REDIRECT_URL = "account_home"

LOGOUT_REDIRECT_URL = "/"

LOGIN_URL = "account_login"

LOGOUT_URL = "account_logout"


# Messages

# MESSAGE_TAGS = {
#    messages.DEBUG: "DEBUG",
#    messages.ERROR: "ERROR",
#    messages.INFO: "INFO",
#    messages.SUCCESS: "SUCCESS",
#    messages.WARNING: "WARNING",
# }


# Sessions

TIME = 240 * 60

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = TIME

SESSION_IDLE_TIMEOUT = TIME


# Static Files

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  # noqa

# STATIC_ROOT = BASE_DIR / "static"  # noqa


# Locale

LANGUAGE_CODE = "en-IN"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True

# Site

SITE_ID = 1
