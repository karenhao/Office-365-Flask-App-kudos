import requests
import json

from . import (
    app,
    db
)
import flask
from .models import O365OAuthToken
from .oauth_helpers import (
    datetime_from_timestamp,
    get_oauth_token,
    get_jwt_from_id_token,
    sign_in_url
)


@app.route('/')
def hello_world():
    return flask.render_template('home.html', o365_sign_in_url=sign_in_url())


@app.route('/connect/get_token/')
def connect_o365_token():
    code = flask.request.args.get('code')
    if not code:
        app.logger.error("NO 'code' VALUE RECEIVED")
        return flask.Response(status=400)

    token = get_oauth_token(code)

    # saves access token to db
    app.logger.info('CREATING new O365OAuthToken')
    oauth_token = O365OAuthToken(
        access_token=token['access_token']
    )
    print(oauth_token)

    print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.create_all()
    db.session.add(oauth_token)
    db.session.commit()

    return 'got the token'


@app.route('/add')
def add_row():
    token = O365OAuthToken.query.all()[0]
    print(token)

    url = 'https://graph.microsoft.com/v1.0/me/drive/root:/kudos.xlsx:/workbook/tables/Table1/rows/add'
    headers = {"Authorization":"Bearer " + token.access_token}
    data = {"index": None, "values": [['J Stray','C','11-Jan','','']]}

    print(requests.post(url,json=data,headers=headers).json())

    return 'added a row'

    # oauth_token = O365OAuthToken.query.filter(O365OAuthToken.user_email == jwt['upn']).first()
    # if not oauth_token:
    #     app.logger.info('CREATING new O365OAuthToken for {}'.format(jwt['upn']))
    #     oauth_token = O365OAuthToken(
    #         access_token=token['access_token'],
    #         refresh_token=token['refresh_token'],
    #         expires_on=datetime_from_timestamp(token['expires_on']),
    #         user_email=jwt['upn'],
    #         token_type=token['token_type'],
    #         resource=token['resource'],
    #         scope=token['scope']
    #     )
    #     db.session.add(oauth_token)
    # else:
    #     app.logger.info('UPDATING existing O365OAuthToken for {}'.format(jwt['upn']))
    #     oauth_token.access_token = token['access_token']
    #     oauth_token.refresh_token = token['refresh_token']
    #     oauth_token.expires_on = datetime_from_timestamp(token['expires_on'])
    #     oauth_token.token_type = token['token_type']
    #     oauth_token.resource = token['resource']
    #     oauth_token.scope = token['scope']

    # db.session.commit()

    # flask.session['user_email'] = oauth_token.user_email
    # flask.session['access_token'] = oauth_token.access_token 
