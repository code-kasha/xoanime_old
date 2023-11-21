import os
from .authentication import *  # noqa

# Host

ALLOWED_HOSTS = []
ALLOWED_HOSTS += os.environ.get("ALLOWED_HOST")


# Database

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABSE_ENGINE"),
        "NAME": os.environ.get("DATABSE_NAME"),
        "USER": os.environ.get("DATABSE_USER"),
        "PASSWORD": os.environ.get("DATABSE_PASSWORD"),
        "HOST": os.environ.get("DATABSE_HOST"),
        "PORT": os.environ.get("DATABSE_PORT"),
    }
}

# E-mail

EMAIL_BACKEND = os.environ.get("EM_BACKEND")

EMAIL_HOST = os.environ.get("EMAIL_HOST")

EMAIL_PORT = os.environ.get("EMAIL_PORT")

EMAIL_USE_TLS = str(os.environ.get("EMAIL_TLS")) == "1"

EMAIL_USE_SSL = str(os.environ.get("EMAIL_SSL")) == "1"

EMAIL_HOST_USER = os.environ.get("EMAIL_USER")

EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASS")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Secret Key

SECRET_KEY = os.environ.get("SECRET_KEY")
