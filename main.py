from typing import Callable
import matplotlib.pyplot as plt
import numpy as np

class NewtonRaphson:

    def __init__(self, func: Callable[[float], float], a1: float) -> None:
        self.f = func
        self.a = a1

    
    def iterate(self):
        self.a = self.a - (self.func())/(self.deriv())
        return self.a

    def func(self, h=0):
        return self.f(self.a+h)
    
    def deriv(self):
        h = 0.0001
        return (self.func(h) - self.func())/h

def sqaure(x: float) -> float:
    return x**2 - 2*x - 4

test = NewtonRaphson(sqaure,10)

t = np.linspace(-10,10,10000)
fig, ax = plt.subplots()
ax.plot(t,sqaure(t))
x = []
y = []
for i in range(10):
    x += [test.a,test.a]
    y += [0, test.func()]
    test.iterate()
ax.spines['left'].set_position('zero')

ax.plot(x,y)
# turn off the right spine/ticks
ax.spines['right'].set_color('none')
ax.yaxis.tick_left()

# set the y-spine
ax.spines['bottom'].set_position('zero')

# turn off the top spine/ticks
ax.spines['top'].set_color('none')
ax.xaxis.tick_bottom()
fig.show()
input()