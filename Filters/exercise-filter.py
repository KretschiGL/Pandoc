#!/usr/bin/env python

"""
Pandoc filter that replaces content that is within a "SOLUTION" comment.
Comments are kept, but all other content is removed.
"""

from pandocfilters import toJSONFilter 
import re

ignoreSolution = False

def exercises(key, value, format, meta):
    global ignoreSolution
    p_begin = re.compile("<!-- BEGIN SOLUTION -->")
    p_end = re.compile("<!-- END SOLUTION -->")
    p_comment = re.compile("<!-- .* -->")
    if key == "RawBlock":
        fmt, s = value
        if p_begin.match(s):
            ignoreSolution = True
            return []
        if p_end.match(s):
            ignoreSolution = False
            return []
        if p_comment.match(s):
            return None
    if ignoreSolution:
        return []

if __name__ == "__main__":
    toJSONFilter(exercises)