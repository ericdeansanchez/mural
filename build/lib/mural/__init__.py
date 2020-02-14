# -*- coding: utf-8 -*-
"""
imgix
~~~~~

A Python micro library for manipulating palette colors:
"""

from .__version import __version__

from .css import CssColor, RgbValue, RankedRgb

__all__ = ['CssColor', 'RgbValue', 'RankedRgb', '__version__', ]
