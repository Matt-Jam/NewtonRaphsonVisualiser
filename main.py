from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

class NewtonRaphson:

    def __init__(self, func: Callable[[float], float], a1: float) -> None:
        self.f = func
        self.a = a1
    
    def iterate(self):
        self.a = self.a - (self.func())/(self.deriv())

    def func(self, h=0) -> float:
        return self.f(self.a+h)
    
    def deriv(self) -> float:
        h = 0.0001
        return (self.func(h) - self.func())/h

    def visualise(self,lower_bound: int =0, upper_bound: int = 10, depth: int = 10) -> None:
        t = np.linspace(lower_bound, upper_bound, abs(upper_bound-lower_bound)*100)
        fig, ax = plt.subplots()
        ax.plot(t,self.f(t))
        
        x = []
        y = []

        for i in range(depth):
            x += [self.a, self.a]
            y += [0, self.func()]
            self.iterate()
        
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

test = NewtonRaphson(square,10)
test.visualise(-20,20,10)
