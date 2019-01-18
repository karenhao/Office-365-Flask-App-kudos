import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
SERVER_ADDRESS = 'http://localhost:5000'

DEBUG = True
SECRET_KEY = '<SECRET>'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.join(BASEDIR, 'database'), 'office365.db')
print(SQLALCHEMY_DATABASE_URI)

SQLALCHEMY_TRACK_MODIFICATIONS = False

O365_APP_ID = 'bd7d7f09-6bc2-40f6-91e3-969604f989ce'
O365_APP_KEY = 'eoD$D(kd-L5>_:K=uSIwA-(g4b|Y{e(v!+t}yK'
O365_REDIRECT_URI = os.path.join(SERVER_ADDRESS, 'connect/get_token')
O365_AUTH_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/authorize'
O365_TOKEN_URL = 'https://login.microsoftonline.com/common/oauth2/v2.0/token'
