from local_settings import * to settings.py 
#Django registration settings
ACCONUT_ACTIVATION_DAYS = 7

# Email setting for seding account activation mails
EMAIL_USE TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "user@example.com"
EMAIL_HOST_PASSWORD = "secret"
EMAIL_PORT = 587