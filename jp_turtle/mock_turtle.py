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

def undefined_mock_operation(_name):
    print("Stubbing out", _name)
    def stub(*args, **kwargs):
        print (_name, "is not implemented for mock turtle")
    return stub

def mock_turtle():
    print("Now replacing standard turtle.py functionality with jp_turtle functionality or stubs.")
    turtle.Turtle = jp_turtle.Turtle
    turtle.Pen = jp_turtle.Turtle
    turtle.Screen = screen.FakeScreen
    turtle.tracer = undefined_mock_operation("tracer")
    turtle.colormode = undefined_mock_operation("colormode")

