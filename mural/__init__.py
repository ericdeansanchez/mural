# -*- coding: utf-8 -*-
"""
Mural
~~~~~

A Python micro library for manipulating palette colors:
"""

from .__version import __version__

from .color import CssColor, RgbValue, RankedRgb

__all__ = ['CssColor', 'RgbValue', 'RankedRgb', '__version__', ]
