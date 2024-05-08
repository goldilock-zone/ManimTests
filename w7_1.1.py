from manim import *
import numpy as np
import random

class CirclePacking(Scene):
    def construct(self):
        # Define parameters
        num_circles = 200
        max_radius = 1.0
        min_radius = 0.1
        max_color_value = 1.0
        colors = [BLUE, RED, GREEN, YELLOW, PURPLE, ORANGE]

        # Function to check if two circles overlap
        def overlap(circle1, circle2):
            return np.linalg.norm(circle1.get_center() - circle2.get_center()) < circle1.radius + circle2.radius

        # Create circles
        circles = []
        for _ in range(num_circles):
            radius = random.uniform(min_radius, max_radius)
            color = random.choice(colors)
            circle = Circle(radius=radius, color=color, fill_opacity=1)
            # Position the circle avoiding overlap
            while any(overlap(circle, other_circle) for other_circle in circles):
                circle.shift(np.array([random.uniform(-5, 5), random.uniform(-3, 3), 0]))
            circles.append(circle)

        # Add circles to the scene
        for circle in circles:
            self.add(circle)

        self.wait()

# To render the scene
# python -m manim your_file.py CirclePacking -p -ql


if __name__ == "__main__":
    scene = CirclePacking()
    scene.render()
