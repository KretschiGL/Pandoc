#!/usr/bin/env python

"""
Pandoc filter replacing a comment <!-- TAB --> with a Tab for *.docx documents.
"""

from pandocfilters import toJSONFilter, RawInline
import re

def tabs(key, value, format, meta):
    p = re.compile("<!-- TAB -->")
    if key == "RawInline":
        fmt, s = value
        if p.match(s):
            return handle_tab(format)

def handle_tab(format):
    if format == "docx":
        return RawInline("openxml", "<w:r><w:tab/></w:r>")

if __name__ == "__main__":
    toJSONFilter(tabs)
