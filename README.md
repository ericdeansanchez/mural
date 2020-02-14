# Mural

## A Micro Library For Wrangling Color Palettes

## Table Of Contents
- [Mural](#mural)
  - [A Micro Library For Wrangling Color Palettes](#a-micro-library-for-wrangling-color-palettes)
  - [Table Of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Quick Start](#quick-start)


### Overview

You want to put paint on the page quickly **_and_** you want it to look good. So you
use some color pickers, edit your stylesheets,  `cmd-c`, `cmd-v`, `cmd-r`, maybe restart
a dev-server.

This isn't that. 

**Mural** aims to be a library for wrangling color palettes. The goal is to combine a [few](https://webaim.org/resources/contrastchecker/) [great](https://docs.imgix.com/apis/url/color-palette/palette) [ideas](https://github.com/w3c/wcag/issues/695) into a library of code that allows developers to build their own palette wrangling workflows.


### Quick Start


Starting with a the first library primitive, `Palette`, let's assume the following project structure:

```
examples/quick-start
├── index.html
└── style.css
```

Now, let's say we want to explore some of our styles programmatically.

```python
>>> from color import Palette
>>> 
>>> # Use the palette to extract colors from a stylesheet.
... # The values returned by `from_styles` are sorted from
... # darkest to lightest (i.e. #000000 to #ffffff).
... 
>>>
>>> palette = Palette()
>>> css_colors = palette.from_styles('style.css')
>>> 
>>> 
>>> css_colors
[CssVale(
    name=image-fg-ex-2, 
    attr=color, 
    value=RgbValue(r=0, g=0, b=0), 
    priority=!important
    ),...
CssVale(
    name=image-bg-vibrant-dark, 
    attr=background-color, 
    value=RgbValue(r=1, g=147, b=15),
    priority=!important
),
CssVale(
    name=image-fg-3, 
    attr=color, 
    value=RgbValue(r=0, g=153, b=23), 
    priority=!important
    ), ...]
>>>
```

Okay cool, but actually, let's deal with some `RgbValue`s
