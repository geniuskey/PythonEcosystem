from asciimatics.widgets import Frame, TextBox, Layout, Label
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError

def demo(screen):
    frame = Frame(screen, int(screen.height * 2 // 3), int(screen.width * 2 // 3), has_border=True)
    layout = Layout([1], fill_frame=True)
    frame.add_layout(layout)
    layout.add_widget(Label("Hello, World!"))
    layout.add_widget(TextBox(5, label="Input:"))
    frame.fix()

    scenes = [Scene([frame], -1)]
    screen.play(scenes, stop_on_resize=True)

try:
    Screen.wrapper(demo)
except ResizeScreenError:
    pass