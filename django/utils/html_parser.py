from html.parser import HTMLParser as _HTMLParser


class HTMLParseError(Exception):
    pass


class HTMLParser(_HTMLParser):
    """Explicitly set convert_charrefs to be False.

    This silences a deprecation warning on Python 3.4, but we can't do
    it at call time because Python 2.7 does not have the keyword
    argument.
    """
    def __init__(self, convert_charrefs=False, **kwargs):
        _HTMLParser.__init__(self, convert_charrefs=convert_charrefs, **kwargs)
