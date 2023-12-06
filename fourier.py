import math
import matplotlib.pyplot as plt
import numpy as np



############################################
# Change these

TERMS = 10

START = -math.pi
END = math.pi

def actual_function(x):
    return x


# Constant term
a_0 = 0

# Coefficients of the cosine terms
def a_n(n):
    return 0

# Coeffients of the sine terms
def b_n(n):
    return -2 * math.cos(n*math.pi) / n


#############################################




def fourier_series(a_0, a_n, b_n, terms=TERMS):
    """
    Returns a function that calculates the Fourier series approximation of a given function.

    Parameters:
    a_0 (float): The DC offset of the function.
    a_n (function): A function that takes an integer n and returns the coefficient of the cosine term with frequency n.
    b_n (function): A function that takes an integer n and returns the coefficient of the sine term with frequency n.
    terms (int): The number of terms to use in the Fourier series approximation.

    Returns:
    function: A function that takes a single argument x and returns the value of the Fourier series approximation at x.
    """
    
    def f_x(x):
        value = a_0 / 2
        for n in range(1, terms+1):
            value += a_n(n) * np.cos(n * x) + b_n(n) * np.sin(n * x)
        return value

    return f_x


# Generate x values
x = np.linspace(START, END, 400)

# Generate y values
fourier_approx = fourier_series(a_0, a_n, b_n)
y = fourier_approx(x)

# Plot the graph
plt.plot(x, y)
plt.plot(x, actual_function(x))
plt.show()
