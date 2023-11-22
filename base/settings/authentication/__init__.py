LOGIN_REDIRECT_URL = "account_home"

LOGOUT_REDIRECT_URL = "/"

LOGIN_URL = "account_login"

LOGOUT_URL = "account_logout"


ACCOUNT_LOGOUT_REDIRECT_URL = LOGOUT_REDIRECT_URL

ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL

from .account import *  # noqa

# from .socialaccount import *  # noqa

# from .mfa import *  # noqa

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
