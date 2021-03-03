#!/usr/bin/env python

"""
Pandoc filter to read a comment that contains a JSON object.
The object is then parsed and used to modify the structure.

{
    "Lines": *number of paragraphs to generate*
}

"""

from pandocfilters import toJSONFilter, Para, Str
import re
import json

def structures(key, value, format, meta):
    p = re.compile("<!-- (?P<options>\{.*\}) -->")
    if key == "RawBlock":
        fmt, s = value
        m = p.match(s)
        if m:
            return handle_options(m.group("options"))

def handle_options(optStr):
    try:
        result = []
        opt = json.loads(optStr)
        result = handle_opt_lines(opt, result)
        return result
    except:
        return []

def handle_opt_lines(opt, result):
    key = "Lines"
    if key in opt:
        try:
            line = int(opt[key])
            result.extend([Para([Str("")]) for _ in range(line)])
        except:
            pass
    return result

if __name__ == "__main__":
    toJSONFilter(structures)
