from LIB import *

x, y = pylab.loadtxt(".dati6.txt", unpack = True)

pylab.errorbar(x, y)

pylab.show()
