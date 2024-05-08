from manim import *
import numpy as np

class ConcentricDots(Scene):
    def construct(self):
        # Parameters
        num_dots = 200  # Number of dots
        max_radius = 2  # Maximum radius
        min_radius = 0.1  # Minimum radius
        center = ORIGIN  # Center of the dots
        density_factor = 3  # Factor to control the density (adjust as needed)
        
        # Create concentric dots
        dots = VGroup()
        for i in range(num_dots):
            radius = self.get_radius(i, num_dots, max_radius, min_radius, density_factor)
            dot = Dot(radius=radius, color=self.get_color(i, num_dots))
            dots.add(dot)
        
        # Arrange dots
        self.arrange_dots(dots)

        # Add to scene
        self.add(dots)

    def get_radius(self, dot_index, num_dots, max_radius, min_radius, density_factor):
        """
        Calculate the radius of a dot based on its index and the cosine of the index.
        """
        angle = dot_index / num_dots * 5
        cosine_density = (np.cos(angle) + 1) / 2  # Adjust to [0, 1]
        radius_range = max_radius - min_radius
        radius = min_radius + cosine_density * radius_range * density_factor
        return radius

    def get_color(self, dot_index, num_dots):
        """
        Generate a random color for each dot.
        """
        if dot_index == num_dots - 1:  # Largest dot
            return BLACK
        else:
            return np.random.rand(3)  # Random RGB color

    def arrange_dots(self, dots):
        """
        Arrange dots in a concentric pattern.
        """
        for i, dot in enumerate(dots):
            dot.move_to(ORIGIN)

if __name__ == "__main__":
    scene = ConcentricDots()
    scene.render()
