#!/usr/bin/env python

import Tkinter, tkFileDialog
import numpy as np

root = Tkinter.Tk()
root.withdraw()

# select file in window
read_file_path = tkFileDialog.askopenfilename()

# read the file
t, x, y, z = np.loadtxt(read_file_path, unpack=True)

write_file_path = tkFileDialog.asksaveasfilename(defaultextension=".txt")

file = open(write_file_path, 'a')

dt = 0.01
for i in range(len(t)):
	if (i != 0):
		t[i] = t[i-1] + dt
	printstr = '%f %f %f %f\n' % (t[i], x[i], y[i], z[i])
	file.write(printstr)

file.close()

