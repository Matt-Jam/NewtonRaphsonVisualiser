""" Module for visualising the Newton Raphson method on a function """
from typing import Callable
import math
import matplotlib.pyplot as plt
import numpy as np

class NewtonRaphson:
    """Class for visualising the newton raphson method applied to a function
    """
    def __init__(self, func: Callable[[float], float]) -> None:
        """Initialises a Newton Raphson object

        Args:
            func (Callable[[float], float]): The function you want to estimate the derivative of
        """
        self.f = func
        self.a = 0

    def iterate(self):
        """Iterates to the next estimation
        """

        self.a = self.a - (self.func())/(self.deriv())

    def func(self, h=0) -> float:
        """Applies the function to the current value of the sequence

        Args:
            h (int, optional): A small offset value used to estimate the derivative. Defaults to 0.

        Returns:
            float: The value of the function at self.a + h
        """
        return self.f(self.a+h)

    def deriv(self) -> float:
        """Calculates the derivative at self.a via approximation

        Returns:
            float: The derivative
        """
        h = 0.0001
        return (self.func(h) - self.func())/h

    def visualise(self,a1: int,lower_bound: int =0, upper_bound: int = 10, depth: int = 10) -> None:
        """Visualise the Newton raphson method applied to this function.

        Args:
            a1 (int): The initial guess
            lower_bound (int, optional): The lower bound for the visualisation. Defaults to 0.
            upper_bound (int, optional): The upper bound for the visualisation. Defaults to 10.
            depth (int, optional): The max number of iterations. Defaults to 10.
        """
        self.a = a1

        t = np.linspace(lower_bound, upper_bound, abs(upper_bound-lower_bound)*100)
        fig, ax = plt.subplots()

        # Plot the function
        ax.plot(t, list(map(self.f, t)))

        x = []
        y = []

        # Calculates the points used for the Newton raphson visualisation
        for _ in range(depth):
            p = self.func()
            # Prevents the visualisation from breaking if the method does not converge
            
            if ((p > upper_bound * 2) or ((p < lower_bound * 2))):
                break
            x += [self.a, self.a]
            y += [0, self.func()]

            try:
                self.iterate()
            except ZeroDivisionError:
                break

        ax.plot(x,y)

        ax.spines['left'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.yaxis.tick_left()
        ax.spines['bottom'].set_position('zero')
        ax.spines['top'].set_color('none')
        ax.xaxis.tick_bottom()

        fig.show()
        input()



def square(x: float) -> float:
    return x**2 - 2*x - 4

def t1(x: float) -> float:
    if x == 0:
        return 0

    return x/math.sqrt(abs(x))
test = NewtonRaphson(t1)

test.visualise(2,-3,3,10)
