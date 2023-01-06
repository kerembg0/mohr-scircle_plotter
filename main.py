from math import sqrt , atan, degrees, cos, sin, radians
import numpy as np
import matplotlib.pyplot as plt

sigma_x = float(input("sigma_x = "))
sigma_y = float(input("sigma_y = "))
to_xy = float(input("tau_xy = "))
rotation_degree = float(input("rotation degre = "))

center = (sigma_x + sigma_y) / 2
radius = sqrt(((sigma_x - sigma_y) / 2)**2 + to_xy**2)

sigma_1 = center + radius
sigma_2 = center - radius

two_alfa = -degrees(atan(2 * to_xy/(sigma_x - sigma_y)))

#plotting the mohr circle
x = np.linspace(center-radius,center+radius,1000)
y = np.sqrt((radius + center - x) * (radius - center + x))
plt.plot(x, y, "b")
plt.plot(x,-y, "b")
plt.gca().set_aspect('equal')

#plotting x-y axises
plt.axhline(0,color='red')
plt.axvline(0,color='red')

#scattering points
points_x = [sigma_2, center, sigma_1, center, center]
points_y = [0,0,0, radius, -radius]
plt.scatter(points_x, points_y, c ="black")

#plotting N-K line
line_x = [cos(radians(two_alfa))*radius + center, cos(radians(two_alfa+180))*radius + center]
line_y = [sin(radians(two_alfa))*radius, sin(radians(two_alfa+180))*radius]

plt.plot(line_x, line_y, color = 'green', marker = "o", label = "Original Stress")

#plotting rotated N-K line
if rotation_degree != 0:
    line_x_r = [cos(radians(two_alfa+2*-rotation_degree))*radius + center, cos(radians(two_alfa+180+2*-rotation_degree))*radius + center]
    line_y_r = [sin(radians(two_alfa+2*-rotation_degree))*radius, sin(radians(two_alfa+180+2*-rotation_degree))*radius]

    plt.plot(line_x_r, line_y_r, color = 'purple', marker = "o", label = "Transformed Stress")

plt.xlabel("σ (N/mm^2)")
plt.ylabel("τ (N/mm^2)")
plt.title("Mohr's Circle")
plt.legend(loc = "upper right")
plt.grid()
plt.show()