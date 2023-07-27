import math


def polar_to_cartesian(length, theta, initial_position=(0, 0)):
    return (
        initial_position[0] + length * math.cos(theta),
        initial_position[1] + length * math.sin(theta)
    )
