
import matplotlib.pyplot as plt
import numpy as np
from sympy.abc import n, l, r, Z
from sympy.physics import hydrogen
from sympy.utilities.lambdify import lambdify

a = 5.29 * 10 ** -11
#taking n, l values to plot 
n = int(input("Enter n:"))
l = int(input("Enter l:"))
R_nl = lambdify(r, hydrogen.R_nl(n, l, r, 1))
r = np.linspace(0,30, 1000)
plt.grid(True)
plt.xlabel("r")
plt.ylabel("R(r)")
#plotting the graph R(r)(radial wave function ) vs r
plt.plot(r, R_nl(r))
#to display the n, l values on the plot
eq = "n="+ str(n)+ ", l="+str(l)
p= (R_nl(0)+R_nl(12))/2                                   
plt.text(6,p,eq, bbox=dict(facecolor='red', alpha=0.5))


##im sree adding other features
