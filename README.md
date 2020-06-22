# jp_turtle

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/lingruiluo/jp_turtle/master)

`jp_turtle` is adapted from the Python turtle programming. It is designed to make it easy to program turtle graphics on Jupyter interface, supported by [`jp_doodle`](https://github.com/AaronWatters/jp_doodle) module which makes implementing special purpose interactive visualizations easy.

<p align="center">
  <img src="/pics/square_gif.gif" width="350" height="350" />
</p>

<br>

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

<br>

## Turtle Graphics

Turtle graphics are vector graphics using a 'turtle' to control movement and direction. They can be complex patterns consisting of many simple graphics. It is one of the feature of [Logo programming language](https://en.wikipedia.org/wiki/Logo_(programming_language)#Turtle_and_graphics) is Please click the [link](https://en.wikipedia.org/wiki/Turtle_graphics) to read more.

<br>

## Examples

**Quick References:** Please see the [document](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/jp_turtle%20quick%20reference.ipynb) to quick start. It will be covering basic functions provided by `jp_turtle`.  
- **Movement**: distance, direction, speed  
- **Icon (cursor or 'turtle')**: shape, color, size, hide, show 
- **Pen**: color, linewidth, up, down
- **Screen**: background color, click movement event  

**Note: The following examples are executable Jupyter notebooks and are supposed to run interactively cell-by-cell.**

|||        
| - | - |   
|<img src="/pics/nautilus.png" width="150" height="150" />| **[Nautilus](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Nautilus%20example.ipynb)**<br>The nautilus pattern consists of quares.<br> It can be drawn starting from a bigger square and by adjusting squares' direction and decreasing side length.|
|<img src="/pics/rainbow square.png" width="150" height="150" />| **[Rainbow Square](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Drawing%20Graphics.ipynb)**<br>The rainbow square example uses 7 rainbow colors. The squares will be drawn with increasing movement distance.|  
|<img src="/pics/tri_spiral1.png" width="150" height="150" /><br><img src="/pics/tri_spiral2.png" width="150" height="150" />|**[Triangle Spirals](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Triangle%20Spiral.ipynb)**<br>The spiral made of triangles.|
|<img src="/pics/square_pattern.png" width="150" height="150" />|**[Circle Examples](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Circle%20examples.ipynb)**<br>This notebook contains several way to create circle patterns. The picture on the left side displays the pattern using 8 3-square patterns with different colors.|
|<img src="/pics/random_walk.png" width="150" height="150" />|**[Random Walk](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Random%20Walk.ipynb)**<br> This example simulates random walk. |
|<img src="/pics/firework.png" width="150" height="150" />|**[Firework](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Firework.ipynb)**<br> Fireworks with different colors. |
|<img src="/pics/sunflower.png" width="150" height="150" />|**[Sunflower](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Sunflower.ipynb)**<br> Sunflower example |
|<img src="/pics/signal_pattern.png" width="150" height="150" />|**[No Signal TV Pattern](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/No%20Signal%20TV%20Pattern.ipynb)**<br> No signal tv pattern |
|<img src="/pics/clock.png" width="150" height="150" />|**[Clock](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/Clock.ipynb)**<br> The example shows the current time on the screen. |
|<img src="/pics/bytedesign.png" width="150" height="150" />|**[bytedesign](https://github.com/lingruiluo/jp_turtle/blob/master/notebooks/bytedesign.ipynb)**<br> Adapted from python turtle bytedesign. |
