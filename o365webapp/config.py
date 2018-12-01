import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
SERVER_ADDRESS = '<URL_FOR_SERVER>'

DEBUG = True
SECRET_KEY = '<SECRET>'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.join(BASEDIR, 'database'), 'office365.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

O365_APP_ID = '<APP ID>'
O365_APP_KEY = '<APP KEY>'
O365_REDIRECT_URI = os.path.join(SERVER_ADDRESS, 'connect/get_token')
O365_AUTH_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
O365_TOKEN_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
