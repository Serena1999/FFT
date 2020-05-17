from LIB import *

x, y = pylab.loadtxt("data_triangolare/datilunghitriangolare.txt", unpack = True)

pylab.errorbar(x, y)

pylab.show()
