'''
set up initial screen
'''

from jp_doodle import dual_canvas
from IPython.display import display


# The "usual" screen -- this gets initialized when needed
USUAL_SCREEN = None
WIDTH = HEIGHT = 400
debugging = True

def get_usual_screen(width=WIDTH, height=HEIGHT):
    global USUAL_SCREEN
    if USUAL_SCREEN is not None:
        return USUAL_SCREEN
    screen = dual_canvas.DualCanvasWidget(width=width, height=height)
    # use a counter to distinguish turtles
    screen.turtle_count = 0
    # store info about turtles in the javascript element container
    screen.js_init("""
        element.turtle_info = { };

        element.get_turtle_info = function(id) {
            return element.turtle_info[id];
        };
    """);
    if not debugging:
        display(screen)
        screen.in_dialog()
        screen.element.dialog(dict(width=width+100, height=height+100))
    else:
         display(screen.debugging_display())
    screen.rect(0, 0, 400, 400, "#eea",name='Screen')
    screen.fit()
    USUAL_SCREEN = screen
    return screen

def reset():
    global USUAL_SCREEN
    USUAL_SCREEN = None

def bgcolor(screen, color):
    screen.change(name='Screen',color=color)

class FakeScreen:
    
    def __repr__(self):
        return "FakeScreen"

    def __getattr__(self, attr):
        print("FakeScreen getattr")
        def dummy_function(*arguments):
            return "not a real method, just a fake: " + repr(attr)
        return dummy_function