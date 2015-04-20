#!/usr/bin/env python

# Takes data from a text file and plots it
# NOTE: basic version does not use test timestamps / labels

import sys
# from pylab import *
import numpy as np
import matplotlib.pyplot as plt 

filename = sys.argv[1]

#t, x, y, z = np.loadtxt(filename)
print np.loadtxt(filename)
x, y, z = np.loadtxt(filename, unpack=True)

tstep = 0.02
t = tstep*np.linspace(0, len(x), len(x))

plt.subplot(3,1,1)
plt.plot(t,x,'r-')
plt.title('Angular Velocity Measurements')
plt.ylabel('Angular Rate x (dps)')

plt.subplot(3,1,2)
plt.plot(t,y,'g-')
plt.ylabel('Anglar Rate y (dps)')

plt.subplot(3,1,3)
plt.plot(t,z,'b-')
plt.ylabel('Angular Rate z (dps)')

plt.show()
