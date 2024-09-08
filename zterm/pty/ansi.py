"""ANSI escape sequence utilities."""

import re
from ansi2html import Ansi2HTMLConverter

SEQ = re.compile(r"\x1b(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
NEWLINE = re.compile(r"\x1b\[\d+\;1H")

conv = Ansi2HTMLConverter(inline=True)

def convert_ansi_to_html(ansi):
    return conv.convert(ansi.replace("\n", ''))

def strip_ansi_escape_sequences(string):
    return SEQ.sub("", string)


def replace_newline(string):
    return NEWLINE.sub("\n", string)
