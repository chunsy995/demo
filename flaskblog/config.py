import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    TRACK_USAGE_USE_FREEGEOIP = True
    TRACK_USAGE_FREEGEOIP_ENDPOINT = 'http://extreme-ip-lookup.com/json/{ip}'
    TRACK_USAGE_INCLUDE_OR_EXCLUDE_VIEWS = 'include'
    TRACK_USAGE_COOKIE = True
