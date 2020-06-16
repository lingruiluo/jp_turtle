"""
shape install
"""


class Shape:
    
    def __init__(self, kind, data):
        self.kind = kind
        self.data = data

    def install(self, in_turtle):
        kind = self.kind
        if kind == "polygon":
            in_turtle.icon_points = [[x, y] for [y, x] in self.data]
            in_turtle.icon_points = [[x*in_turtle.lineWidth, y*in_turtle.lineWidth] for [x,y] in in_turtle.icon_points]
            in_turtle.forward(0)
        else:
            raise ValueError("unknown kind " + repr(kind))