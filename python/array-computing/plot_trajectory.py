
import numpy as np
import sys

y0 = float(sys.argv[1])
v0 = float(sys.argv[2])
theta = int(sys.argv[3])
g = 9.81
y = x*np.tan(theta) - (1/2*v0**2)*(g*x**2/2*np.cos**2(theta))+y0
