"""
some helper functions
"""

import math

def rotate_translate(x, y, radians, xt, yt):
    s = math.sin(radians)
    c = math.cos(radians)
    xr = x * c - y * s
    yr = x * s + y * c
    return [xr + xt, yr + yt]

def icon_size(x, y, size):
    return [x*(1+(size-1)/10), y*(1+(size-1)/10)]
