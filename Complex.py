## mandelbrot set - set of complex numbers, whose boundary forms a distinctive and intricate pattern when depicted on the complex plane
# fractals - infinitely repeating patterns on different scales

# def z(n, c):
#     if n == 0:
#         return 0
#     else:
#         return z(n - 1, c) ** 2 + c

# for n in range(10):
#     print(f"z{n}: {z(n, 1)}")

## using generator function (yield) : an iterative approach
# yield returns generator object with multiple values and start right from where it left last

""" def sequence(c, z=0):
    for i in range(10):
        yield z
        z = z ** 2 + c
    return z """

#  iteration eliminates redundant function calls for the already-computed sequence elements - not running the risk of hitting the maximum recursion limit anymore
# value of c determines z -> infinity - grow without bound (1), stable (0) - same or within a bounded range, periodically stable (-1) - cycling back and forth b/w the same few values
# stable and periodically stable z -> make up mandelbrot set

# estimated area = 1.506484 sq units
# perimeter = infinite -> coastline paradox

#Julia set - z0 = candidate value, c = fixed constant
""" def mandelbrot(candidate):
    return sequence(z=0, c=candidate)

def julia(candidate, parameter):
    return sequence(z=candidate, c=parameter)

for n, z in enumerate(sequence(c=-1)):
    print(f"z({n}) = {z}")
"""
# world coordinates - continuous spectrum of numbers on the complex plane, extending to infinity
# pixel coordinates - discrete and constrained by the finite size of our screen

import matplotlib.pyplot as plt
import numpy as np

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

#get the z values that would stay stable after many iterations - as they are the ones that belongs to mandelbrot set (like -1)
def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z**2 + c
    return abs(z) <= 2

if __name__ == "__main__":
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=512)

    plt.imshow(is_stable(c, num_iterations=30), cmap="binary")
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

""" def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]


if __name__ == "__main__":
    c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=21)
    members = get_members(c, num_iterations=20)

    plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
    plt.gca().set_aspect("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show() """