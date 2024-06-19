import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cage import Window
import pyglet
from pyglet import shapes

def main():
    window = Window(title = "Test Window")

    # Add a red rectangle
    rectangle = shapes.Rectangle(100, 100, 100, 100, color=(255, 0, 0))
    window.add_shape(rectangle)

    # Add a green circle
    circle = shapes.Circle(300, 300, 50, color=(0, 255, 156))
    window.add_shape(circle)

    # Schedule the update function
    pyglet.clock.schedule_interval(window.update, 1/60.0)

    # Run the application
    pyglet.app.run()

if __name__ == "__main__":
    main()
