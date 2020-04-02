from LIB import *
#import pyFFTW

Directory = "data/ESP_5/"

FileName = "datilunghiquadra.txt"

t, y = pylab.loadtxt(Directory+FileName, unpack = True)

pylab.errorbar(t, y, linestyle = '', marker = 'o', color = 'blue')

pylab.show()

dteff = (max(t) - min(t))/ len(t)

dteff = dteff * (10**6)

print(dteff)

fmax = 1 /(2*dteff)

print(fmax)

dpi = 2.0 * numpy.pi

transf = numpy.fft.fft(y)

retransf = transf.real

freq = numpy.linspace(0., fmax, len(t))

pylab.errorbar(freq, retransf)

pylab.show()

#non ha parte immaginaria

#imtransf = transf.img

#pylab.errorbar(freq, imtransf)

#pylab.show()

transf = abs(transf)

#transf = abs(numpy.fft.rfft(y))

pylab.errorbar(freq, transf)

pylab.show()

print(math.log(len(t), 2))

print(math.log(len(transf), 2))

##Grafico di potenza

ptransf = (transf)**2

pylab.errorbar(freq, ptransf)

pylab.show()

#itransf = abs(numpy.fft.ifft(y))

#pylab.errorbar(t, y, linestyle = '', marker = 'o', color = 'blue')

#pylab.errorbar(t, (max(y)-min(y)) *itransf)

#pylab.show()


