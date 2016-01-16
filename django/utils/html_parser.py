import re

from html import parser


try:
    HTMLParseError = parser.HTMLParseError
except AttributeError:
    # create a dummy class for Python 3.5+ where it's been removed
    class HTMLParseError(Exception):
        pass

class HTMLParser(parser.HTMLParser):
    """Explicitly set convert_charrefs to be False.

    This silences a deprecation warning on Python 3.4, but we can't do
    it at call time because Python 2.7 does not have the keyword
    argument.
    """
    def __init__(self, convert_charrefs=False, **kwargs):
        parser.HTMLParser.__init__(self, convert_charrefs=convert_charrefs, **kwargs)
