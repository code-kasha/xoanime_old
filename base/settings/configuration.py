from .base import *  # noqa

from django.contrib.messages import constants as messages

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-IN"

# MEDIA_URL = "media/"

# MEDIA_ROOT = BASE_DIR / "media"  # noqa

MESSAGE_TAGS = {
    messages.DEBUG: "DEBUG",
    messages.ERROR: "ERROR",
    messages.INFO: "INFO",
    messages.SUCCESS: "SUCCESS",
    messages.WARNING: "WARNING",
}

SITE_ID = 1

SESSION_COOKIE_AGE = 240 * 60

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SERIALIZER = "django.contrib.sessions.serializers.PickleSerializer"

SESSION_IDLE_TIMEOUT = 240 * 60

STATIC_URL = "static/"

STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  # noqa

# STATIC_ROOT = BASE_DIR / "static"  # noqa

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True
