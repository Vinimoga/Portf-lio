import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=true)

def Serie_taylor(func,n_limit,variable = [x]):
    f = lambdify(variable,func)(0)
    for i in range(n_limit-1):
        c = lambdify(variable,diff(func,x,i+1))
        #print(a)
        f = f + (c(0)*x**(i+1))/factorial(i+1)
    #print(f)
    #f = lambdify(variable, f)
    return f

terms = 10             #Change this value to show the terms in the taylor series
func = atan(x)         #Change this value to calculate a different function
t = np.arange(-10, 10, 0.01)

fig, ax = plt.subplots()

ax.set(xlabel='t', ylabel='y', title='Taylor Series Demonstrated')

ax.grid()

s1 = np.vectorize(lambdify([x],Serie_taylor(func,terms)))
s2 = np.vectorize(lambdify([x],func))

ax.plot(t, s1(t), "b-", label=terms)
ax.plot(t, s2(t), "r--")

# limit x by -5 to 5
plt.ylim(-1.5, 1.5)
plt.show()
