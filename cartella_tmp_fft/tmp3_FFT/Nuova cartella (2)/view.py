from LIB import *

x, y = pylab.loadtxt("data_osc_reazione_F/transosc01.txt", unpack = True)

pylab.errorbar(x, y)

pylab.show()
