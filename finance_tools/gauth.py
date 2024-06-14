import sys
from urllib.parse import urlparse
from urllib.error import URLError
from urllib.request import Request, urlopen

from flask import url_for, redirect
from urllib import parse as urlparse
sys.modules["urlparse"] = urlparse
sys.modules["urllib"] = urlparse
from flask_oauth import OAuth

GOOGLE_CLIENT_ID = '446945525351-dpgcaca62kdm11is4etbuec6ft3hjiqu.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'a_PyhMyTePdbgsBa-6k3JV2g'
REDIRECT_URI = '/oauth2callback'  # one of the Redirect URIs from Google APIs console

SECRET_KEY = 'development key'
oauth = OAuth()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)


def authenticate(session):
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]

    headers = {'Authorization': 'OAuth ' + access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo', None, headers)
    try:
        res = urlopen(req)
    except URLError as e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return res.read()

    return res.read()
