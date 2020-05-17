from LIB import *

x, y = pylab.loadtxt("data_sinusoidale_F/sin14.txt", unpack = True)

print(len(x))

pylab.errorbar(x, y)

pylab.show()
