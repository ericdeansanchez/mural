import re
from typing import Iterable

class RgbValue:
    def __init__(self, r, g, b):
        if isinstance(r, str):
            r = int(r, 16)
        if isinstance(g, str):
            g = int(g, 16)
        if isinstance(b, str):
            b = int(b, 16)
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_hex(cls, hex_str: str):
        assert len(hex_str) == 6
        r, g, b = hex_str[:2], hex_str[2:4], hex_str[4:6]
        return RgbValue(r, g, b)
    
    @property
    def relative_luminance(self):
        return (0.2126 * (self.r / 255.0)) + (0.7152 * (self.g / 255.0)) + (0.0722 * (self.b / 255.0))

    def contrast_ratio(self, other, precision):
        assert isinstance(other, RgbValue)
        darker, lighter = sorted([other, self], key=lambda c: c.relative_luminance)
        return round((lighter.relative_luminance + 0.05) / (darker.relative_luminance + 0.05), precision)

    def complement(self, other):
        assert isinstance(other, RgbValue)
        return RgbValue(255.0 - other.r, 255.0 - other.g, 255.0 - other.b)

    def __repr__(self):
        return f'RgbValue(r={self.r}, g={self.g}, b={self.b})'

    def __str__(self):
        return self.__repr__()


class CssColor:
    def __init__(self, name, attr, value, priority):
        self._name = name
        self._attr = attr
        self._value = RgbValue.from_hex(value)
        self._priority = priority

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def attr(self):
        return self._attr

    @attr.setter
    def attr(self, attr):
        self._attr = attr
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = RgbValue.from_hex(value)
    
    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority
    
    @classmethod
    def from_match(cls, m):
        assert len(m) == 4
        return CssColor(m[0], m[1], m[2], m[3])

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'CssVale(name={self.name}, attr={self.attr}, value={self.value}, priority={self.priority})'

class RankedRgb:
    def __init__(self, values: Iterable):
        self.values = sorted(values, key=lambda rgb: rgb.relative_luminance)

pat = r'(?:\.)(?P<css_name>[^ {]+)(?:\s+\{\s+)(?P<attr>[\w\-]+)(?::\s*)(?:[#])(?P<val>[\w]+)(?:\s+)(?P<priority>![\w]+)'


def parse_unique_css_colors(stylesheet):
    css_values = []
    with open('style.css') as f:
        data = f.read()
        found = re.findall(pat, data)
        unique = set()
        css_values = []
        for sought in found:
            if hex(int(sought[2], 16)) in unique:
                continue
            else:
                unique.add(hex(int(sought[2], 16)))
                css_values.append(CssColor.from_match(sought))
    return sorted(css_values, key=lambda c: c.value.relative_luminance)


def parse_css_colors(stylesheet):
    css_values = []
    with open('style.css') as f:
        data = f.read()
        found = re.findall(pat, data)
        css_values = []
        for sought in found:
            css_values.append(CssColor.from_match(sought))
    return sorted(css_values, key=lambda c: c.value.relative_luminance)

def parse_rgb_colors(stylesheet):
    rgb_values = []
    with open(stylesheet) as f:
        data = f.read()
        found = re.findall(pat, data)
        unique = set()
        for sought in found:
            if sought[2] in unique:
                continue
            else:
                unique.add(sought[2])
        for u in unique:
            rgb_values += [RgbValue.from_hex(u)]
    return sorted(rgb_values, key=lambda rgb: rgb.relative_luminance)


def foreground(css_colors: Iterable) -> Iterable:
    fg_colors, FG = [], 'fg'
    for color in css_colors:
        if FG in color.name:
            fg_colors += [color]
    return fg_colors

def background(css_colors: Iterable) -> Iterable:
    bg_colors, BG = [], 'bg'
    for color in css_colors:
        if BG in color.name:
            bg_colors += [color]
    return bg_colors

def muted(css_colors: Iterable) -> Iterable:
    muted_colors, MUTED = [], 'muted'
    for color in css_colors:
        if MUTED in color.name:
            muted_colors += [color]
    return muted_colors