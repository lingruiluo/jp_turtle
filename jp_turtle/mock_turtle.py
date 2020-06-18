"""
Hack the standard Python turtle.py module
to use jp_turtle instead by replacing objects
like turtle.Turtle with jp_turtle equivalent
implementations.

This will not work for all functionality yet.

Execute

>>> mock_turtle()

*before* importing any other modules that import turtle
"""

import turtle
import jp_turtle
from jp_turtle import screen

def mock_turtle():
    turtle.Turtle = jp_turtle.Turtle
    turtle.Pen = jp_turtle.Turtle
    turtle.Screen = screen.FakeScreen

