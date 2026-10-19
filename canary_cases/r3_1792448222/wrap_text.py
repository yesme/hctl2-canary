"""Wrap text to a specified line width."""

import textwrap


def wrap_text(s, w):
    """Return text wrapped to width w with newline-separated lines."""
    return textwrap.fill(s, width=w)
