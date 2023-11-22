from .configuration import *  # noqa
from .authentication import *  # noqa


ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "xo.sqlite3",  # noqa
    }
}

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECRET_KEY = "dzb%v=o%_mkg$ix!^*16pzt%o-uov$ojib0*-qlo9tfr9&j+w#"
