from __future__ import unicode_literals

import sys
from http import cookies

from django.utils.encoding import force_str


# Cookie pickling bug is fixed in Python 2.7.9 and Python 3.4.3+
# http://bugs.python.org/issue22775
cookie_pickles_properly = sys.version_info >= (3, 4, 3)

if cookie_pickles_properly:
    SimpleCookie = cookies.SimpleCookie
else:
    Morsel = cookies.Morsel

    class SimpleCookie(cookies.SimpleCookie):
        def __setitem__(self, key, value):
            # Apply the fix from http://bugs.python.org/issue22775 where
            # it's not fixed in Python itself
            if isinstance(value, Morsel):
                # allow assignment of constructed Morsels (e.g. for pickling)
                dict.__setitem__(self, key, value)
            else:
                super(SimpleCookie, self).__setitem__(key, value)


def parse_cookie(cookie):
    if cookie == '':
        return {}
    if not isinstance(cookie, cookies.BaseCookie):
        try:
            c = SimpleCookie()
            c.load(cookie)
        except cookies.CookieError:
            # Invalid cookie
            return {}
    else:
        c = cookie
    cookiedict = {}
    for key in c.keys():
        cookiedict[key] = c.get(key).value
    return cookiedict
