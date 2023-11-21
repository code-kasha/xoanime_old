from .authentication import *  # noqa

# Hosts

ALLOWED_HOSTS = ["*"]

# Databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "xo.sqlite3",  # noqa
    }
}

# Debug

DEBUG = True

# Email

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Secret Key

SECRET_KEY = "dzb%v=o%_mkg$ix!^*16pzt%o-uov$ojib0*-qlo9tfr9&j+w#"
