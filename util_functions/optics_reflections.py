import numpy as np
from scipy.optimize import root

# Define the system of equations
def intersection(angle):
    def equations(var, slope):
        x, y = var
        # Equation 1: A hyperbola (x^2 - y^2 = 1)
        eq1 = x**2-y**2-1
        # Equation 2: A line passing through (sqrt(2), 0) with a given slope
        eq2 = y - slope * (x - np.sqrt(2))
        return [eq1, eq2]

    # Initial guess
    guess = [-1, 0]


    sol = root(equations, guess, args=(angle,))

    if sol.success:
        return sol.x
    else:
        raise ValueError("scipy solver failed to find a root.")

intersection(0.5)