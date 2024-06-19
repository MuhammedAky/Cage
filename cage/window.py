import pyglet
from pyglet import shapes

class Window(pyglet.window.Window):
    def __init__(self, width=800, height=600, title="Pyglet Window", background_color=(0, 0, 0, 255)):
        super().__init__(width=width, height=height, caption=title)
        self.background_color = background_color

        # Batch for drawing shapes
        self.batch = pyglet.graphics.Batch()

        # Example shapes
        self.shapes = []

        # Set the background color
        self.clear_color = background_color

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def clear(self):
        pyglet.gl.glClearColor(*[c/255 for c in self.background_color])
        pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)

    def add_shape(self, shape):
        self.shapes.append(shape)
        shape.batch = self.batch

    def update(self, dt):
        # Update logic (if any) goes here
        pass
