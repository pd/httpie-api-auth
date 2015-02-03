"""
ApiAuth auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin
import hmac, base64, hashlib, datetime, urlparse

__version__ = '0.1.0'
__author__ = 'Kyle Hargraves'
__licence__ = 'MIT'

class ApiAuth:
    def __init__(self, access_id, secret_key):
        self.access_id = access_id
        self.secret_key = secret_key

    def __call__(self, r):
        content_type = r.headers.get('content-type')
        if not content_type:
            content_type = ''

        content_md5  = r.headers.get('content-md5')
        if not content_md5:
            content_md5 = ''

        httpdate = r.headers.get('date')
        if not httpdate:
            now = datetime.datetime.utcnow()
            httpdate = now.strftime('%a, %d %b %Y %H:%M:%S GMT')
            r.headers['Date'] = httpdate

        url  = urlparse.urlparse(r.url)
        path = url.path
        if url.query:
          path = path + '?' + url.query

        string_to_sign = '%s,%s,%s,%s' % (content_type, content_md5, path, httpdate)
        digest = hmac.new(self.secret_key, string_to_sign, hashlib.sha1).digest()
        signature = base64.encodestring(digest).rstrip()

        r.headers['Authorization'] = 'APIAuth %s:%s' % (self.access_id, signature)
        return r

class ApiAuthPlugin(AuthPlugin):

    name = 'ApiAuth auth'
    auth_type = 'api-auth'
    description = 'Sign requests using the ApiAuth authentication method'

    def get_auth(self, access_id, secret_key):
        return ApiAuth(access_id, secret_key)
