# Mural

## A Micro Library For Wrangling Color Palettes

## Table Of Contents
- [Mural](#mural)
  - [A Micro Library For Wrangling Color Palettes](#a-micro-library-for-wrangling-color-palettes)
  - [Table Of Contents](#table-of-contents)
    - [Overview](#overview)
    - [Goals](#goals)
    - [Quick Start](#quick-start)


### Overview

You want to put paint on the page quickly **_and_** you want it to look good. So you
use some color pickers, edit your stylesheets,  `cmd-c`, `cmd-v`, `cmd-r`, maybe restart
a dev-server.

This isn't that. 

**Mural** aims to be a library for wrangling color palettes. The goal is to combine a [few](https://webaim.org/resources/contrastchecker/) [great](https://docs.imgix.com/apis/url/color-palette/palette) [ideas](https://github.com/w3c/wcag/issues/695) into a library of code that allows developers to build their own palette wrangling workflows.

### Goals

Hey 👋🏼, thanks for stopping by. This was really fun and I wish I had more time to work before showing this off. I started off thinking about the use case. To be honest, I think I have a lot more to learn about this space.

For example, the initial plan was to build a static analysis library that engineers could use to "put a number" on a question like "is this font over this background readable?" I soon found out that [algorithmically gauging perceived contrast ratios is not such an easy thing to do](https://github.com/w3c/wcag/issues/695). No worries.

I had already written a regex to parse some css[0], so I began a little 'color-picker-from-a-color-palette'. Then I noticed you've already got a great one (the imgix sandbox). Cool! But, I still have to keep it going. 

I transitioned to writing the readme, integrating sphinx & tox, and starting some examples/tutorials. If I did it again, I don't think I'd use sphinx again. The goal was to get a nice `readthedocs` site "for free," by simply writing in-code documentation and using sphinx-autodoc extension. It's just one of those things that adds some polish. I also licensed this code with what seems to be the most dev-friendly license: MIT.

In the future, I think I'd try to integrate the features from the sandbox into a packaged cli tool. I see the library going in a few different directions:

- for analysis
  - the library could offer cli tools to check accessibility guidelines/best-practices
  - this is the color-palette + lighthouse + webaim scenario
- for design exploration
  - I was actually surprised to not find a lot of tools to do the above accessibility checks
  - I also think **it would be cool to explore** a bit in a local sandbox environment and keep what looks good.
    - e.g. from something like **`$ mural generate-spec-from <images/>`** you could get back a list of templates.


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
    ), 
...]
>>>
```

Okay cool, but actually, let's deal with some `RgbValue`s instead:

```python
>>> rgb_values = [c.value for c in css_colors]
>>> rgb_values
[RgbValue(r=0, g=0, b=0), 
 RgbValue(r=0, g=0, b=0),
 RgbValue(r=96, g=26, b=15), 
 RgbValue(r=96, g=26, b=15), 
 RgbValue(r=43, g=85, b=47), 
 RgbValue(r=43, g=85, b=47),
 ...
 RgbValue(r=255, g=255, b=255)]
 >>>
```

Contrast ratios range from `1:1` (white on white) to `21:1` (black on white).

```python
>>> black = rgb_values[0]  # the rgb values have been sorted
>>> white = rgb_values[-1] # by relative luminance. 
>>> 
>>> black
RgbValue(r=0, g=0, b=0)
>>> white
RgbValue(r=255, g=255, b=255)
>>> white.contrast_ratio(black)
21.0
>>> white.contrast_ratio(white)
1.0
>>> 
```



[0] I gather that it's probably not wise to parse css in this way. I'd need to find/write a better solution if this kind of route is to be pursued.