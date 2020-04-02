from LIB import *

Directory = "data/ESP_5/"

FileName = "datilunghiquadra.txt"

t, y = pylab.loadtxt(Directory+FileName, unpack = True)

tra = numpy.fft.rfft(y)

#tra = tra.real

tra = abs(tra)

print(len(tra))

f = numpy.linspace(0., 1., len(tra))
#poi vedi come mettere ma hai capito che devi usare abs(tra)

pylab.errorbar(f, tra)

pylab.show()
