from typing import Callable
import matplotlib.pyplot as plt
import numpy as np
import math
class NewtonRaphson:

    def __init__(self, func: Callable[[float], float]) -> None:
        self.f = func
        self.a = 0
    
    def iterate(self):
        self.a = self.a - (self.func())/(self.deriv())

    def func(self, h=0) -> float:
        return self.f(self.a+h)
    
    def deriv(self) -> float:
        h = 0.0001
        return (self.func(h) - self.func())/h

    def visualise(self,a1: int,lower_bound: int =0, upper_bound: int = 10, depth: int = 10) -> None:
        self.a = a1
        t = np.linspace(lower_bound, upper_bound, abs(upper_bound-lower_bound)*100)
        fig, ax = plt.subplots()
        ax.plot(t, list(map(self.f, t)))
        
        x = []
        y = []

        for i in range(depth):
            p = self.func()
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
