#!/usr/bin/env python

"""
Pandoc filter that replaces content that is within an "EXERCISE" comment.
"""

from pandocfilters import toJSONFilter, Div
import re

ignoreExercise = False

def solutions(key, value, format, meta):
    global ignoreExercise
    p_begin = re.compile("<!-- BEGIN EXERCISE -->")
    p_end = re.compile("<!-- END EXERCISE -->")
    if key == "RawBlock":
        fmt, s = value
        if p_begin.match(s):
            ignoreExercise = True
            return []
        if p_end.match(s):
            ignoreExercise = False
            return []
    if ignoreExercise:
        return []

if __name__ == "__main__":
    toJSONFilter(solutions)