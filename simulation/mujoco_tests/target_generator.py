import math
import random


class TargetGenerator:

    @staticmethod
    def linear(step, speed=0.5):
        x = step * speed
        y = 5
        return x, y

    @staticmethod
    def circular(step, radius=10):
        angle = step * 0.1

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        return x, y

    @staticmethod
    def random_walk(x, y, step_size=1):

        x += random.uniform(-step_size, step_size)
        y += random.uniform(-step_size, step_size)

        return x, y

    @staticmethod
    def zigzag(step):

        x = step * 0.5

        if step % 20 < 10:
            y = 5
        else:
            y = -5

        return x, y


if __name__ == "__main__":

    generator = TargetGenerator()

    for step in range(20):

        x, y = generator.circular(step)

        print(
            f"Step {step}: "
            f"Target Position = ({x:.2f}, {y:.2f})"
        )
