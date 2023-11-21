from .configuration import *

ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_CHANGE_EMAIL = False

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

# ACCOUNT_DEFAULT_HTTP_PROTOCOL = "https"

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = LOGIN_URL  # noqa

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = LOGIN_REDIRECT_URL  # noqa

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "optional"  # "mandatory"

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[XO Anime]"

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 180

ACCOUNT_EMAIL_MAX_LENGTH = 254

# ACCOUNT_FORMS = {
#    "add_email": "apps.accounts.forms.AddEmailForm",
#    "change_password": "apps.accounts.forms.ChangePasswordForm",
#    "login": "apps.accounts.forms.LoginForm",
#    "reset_password": "apps.accounts.forms.ResetPasswordForm",
#    "reset_password_from_key": "apps.accounts.forms.ResetPasswordKeyForm",
#    "set_password": "apps.accounts.forms.SetPasswordForm",
#    "signup": "apps.accounts.forms.SignupForm",
#    "user_token": "apps.accounts.forms.UserTokenForm",
# }

ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

ACCOUNT_LOGIN_ON_PASSWORD_RESET = False

ACCOUNT_LOGOUT_ON_GET = False

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

ACCOUNT_LOGOUT_REDIRECT_URL = LOGOUT_REDIRECT_URL  # noqa

ACCOUNT_MAX_EMAIL_ADDRESSES = 5

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

ACCOUNT_PASSWORD_RESET_TOKEN_GENERATOR = (
    "allauth.account.forms.EmailAwarePasswordResetTokenGenerator"
)

ACCOUNT_PRESERVE_USERNAME_CASING = True

ACCOUNT_PREVENT_ENUMERATION = True

ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m",
    "manage_email": "10/m",
    "reset_password": "20/m",
    "reset_password_email": "5/m",
    "reset_password_from_key": "20/m",
    "signup": "20/m",
}

ACCOUNT_SESSION_REMEMBER = None

ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = False

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

ACCOUNT_SIGNUP_REDIRECT_URL = LOGIN_REDIRECT_URL  # noqa

ACCOUNT_TEMPLATE_EXTENSION = "html"

ACCOUNT_USERNAME_BLACKLIST = []

ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

ACCOUNT_USERNAME_MIN_LENGTH = 4

ACCOUNT_USERNAME_REQUIRED = True

ACCOUNT_USERNAME_VALIDATORS = "apps.accounts.validators.UsernameValidator"
