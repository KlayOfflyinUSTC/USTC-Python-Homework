# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 15:09:20 2023

@author: 17740
"""

import math

class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.compute_points()

    def compute_points(self):
        raise NotImplementedError(self.__class__.__name__)

    def integrate(self, f):
        result = 0
        for i in range(self.n + 1):
            result += f(self.points[i]) * self.weights[i]
        return result
        

class Trapezoidal(Integrator):
    def compute_points(self): 
        a,b,n = self.a, self.b ,self.n
        h = (b-a) / n
        points = []
        weights = []
        for i in range(n + 1):
            x = a + i * h
            if (i == 0) + (i == n) == 1 :
                w = h / 2
            else:
                w = h
            points.append(x)
            weights.append(w)
        return points,weights
            
class Simpson(Integrator):
    def compute_points(self):
        a,b,n = self.a, self.b ,self.n
        if n % 2 == 1 :
            n = n + 1
            self.n += 1
        h = (b-a) / n
        points = []
        weights = []
        for i in range(n + 1):
            x = a + i * h
            if (i == 0) + (i == n)== 1 :
                w = h / 3
            elif i % 2 == 0 :
                w = 2 * h / 3
            else :
                w = 4 * h / 3
            points.append(x)
            weights.append(w)
        return points,weights
    
class GaussLegendre(Integrator):
    def compute_points(self):  
        a,b,n = self.a, self.b ,self.n
        if n % 2 == 0 :
            n = n + 1
            self.n += 1
        h = 2 * (b - a) / (n + 1)
        points = []
        weights = []
        for i in range(n + 1):
            if i % 2 == 0 :
                x = a + (i + 1) * h / 2 - math.sqrt(3) * h / 6 
            else :
                x = a + i * h / 2 + math.sqrt(3) * h / 6
            w = h / 2
            points.append(x)
            weights.append(w)
        return points,weights
            

def test():
    def f(x): return (x * math.cos(x) + math.sin(x)) * \
                      math.exp(x * math.sin(x))
    def F(x): return math.exp(x * math.sin(x))

    a = 2; b = 3; n = 200
    I_exact = F(b) - F(a)
    tol = 1E-3

    methods = [Trapezoidal, Simpson, GaussLegendre]
    for method in methods:
        integrator = method(a, b, n)
        I = integrator.integrate(f)
        rel_err = abs((I_exact - I) / I_exact)
        print('%s: %g' % (method.__name__, rel_err))
        if rel_err > tol:
            print('Error in %s' % method.__name__)

if __name__ == '__main__':
    test()