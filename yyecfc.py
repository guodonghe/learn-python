# _*_ coding: utf-8 _*_

import math

def quadratic(a,b,c):
    if (b*b - 4*a*c) < 0:
        return 'None'
    Delte = math.sqrt(b*b-4*a*c)
    if Delte > 0:
        x = (-b+Delte)/(2*a)
        y = (-b-Delte)/(2*a)
        return x,y
    else:
        x = (-b) / (2*a)
        return x

print(quadratic(2,3,1))
print(quadratic(1,3,-4))
