from manim import *
import numpy as np
import random

class SpheresScene(Scene):
    def construct(self):
        # Define parameters
        num_spheres = 200
        max_radius = 1.0
        min_radius = 0.1
        max_color_value = 0.8

        # Create and add spheres to scene
        for i in range(num_spheres):
            radius = random.uniform(min_radius, max_radius)
            if radius == max_radius:
                color = BLACK  # Largest spheres are black
            else:
                color = [int(random.uniform(0, max_color_value) * 255) for _ in range(3)]  # Convert to integers
            sphere = Circle(radius=radius, color=color, fill_opacity=1).shift(np.array([random.uniform(-5, 5), random.uniform(-3, 3), 0]))
            self.add(sphere)

        self.wait()

if __name__ == "__main__":
    scene = SpheresScene()
    scene.render()
