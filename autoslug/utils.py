# -*- coding: utf-8 -*-

import re
import textwrap

def slugify(text, separator='-', wrap_at=40):
    """Create a friendly slug from text using a separator."""
    wrapped_text = textwrap.wrap(text, wrap_at)[0]

    # remove our best guess at apostrophes, since they would produce
    # awkward slugs later on like "i-love-my-mom-s-cooking"
    subbed_text = re.sub(r"(\w+)'(\w+)", r'\1\2', wrapped_text, flags=re.UNICODE)
    
    # this pattern is influenced by the RFC 3986
    # (http://tools.ietf.org/html/rfc3986/) and a thread on SO
    # (http://stackoverflow.com/a/1547940); the reasoning is that
    # a URL with these characters included would confuse users and
    # machines alike, so it's best to replace them; however, we
    # still want Unicode characters in foreign languages to appear
    pattern = r'[^\s\/\?\-\.\[\]\$\+\^\'"_~:#@!&()*,;=%]+'

    # findall() is used instead of sub() or split() because
    # additional logic was required to avoid unfriendly characters
    # at the beginning or end of the string -- e.g. "Hello!" would
    # return "hello-" with sub() and ['hello', ''] with split()
    matches = re.findall(pattern, subbed_text.lower(), re.UNICODE) or [separator]
    
    return separator.join(matches)