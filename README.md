# jp_turtle

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lingruiluo/jp_turtle/master)

`jp_turtle` is adapted from the Python turtle programming. It is designed to make it easy to program turtle graphics on Jupyter interface, supported by [`jp_doodle`](https://github.com/AaronWatters/jp_doodle) module which makes implementing special purpose interactive visualizations easy.

## Installation

To install the package for use with Jupyter Notebook, follow the instructions below.

### Development install

This is for development purpose.

```
pip install -e .
```

### User install

This is for use purpose.

```
pip install git+https://github.com/lingruiluo/jp_turtle.git
```
The module requires `jp_doodle` to implement, you can download the `jp_doodle` package by following
```
pip install git+https://github.com/AaronWatters/jp_doodle.git
```

### User upgrade

```
pip install git+https://github.com/lingruiluo/jp_turtle.git --upgrade
```

## Turtle Graphics

Turtle graphics are vector graphics using a 'turtle' to control movement and direction. They can be complex patterns consisting of many simple graphics. It is one of the feature of [Logo programming language](https://en.wikipedia.org/wiki/Logo_(programming_language)#Turtle_and_graphics) is Please click the [link](https://en.wikipedia.org/wiki/Turtle_graphics) to read more.

## Examples

**Quick References:** Please see the [document](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/jp_turtle%20quick%20reference.ipynb) to quick start.  
It will be covering basic functions provided by `jp_turtle`.  
- **Movement**: distance, direction, speed  
- **Icon (cursor or 'turtle')**: shape, color, size, hide, show 
- **Pen**: color, linewidth, up, down
- **Screen**: background color, click movement event

----------|----------
|[Nautilus](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Nautilus%20example.ipynb)
|[Rainbow Square](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Drawing%20Graphics.ipynb)
