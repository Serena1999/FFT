from LIB import *

Directory = "data/ESP_5/"

FileName = "datilunghiquadra.txt"

t, y = pylab.loadtxt(Directory+FileName, unpack = True)

dt = t * 0. + 4 #microsecondi

dy = y * 0. + 1 #digit

pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')

pylab.show()

gridsize = (3, 1)

g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)

g2 = plt.subplot2grid(gridsize,(2,0), colspan = 2)

g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')

g1.set_title("Onda quadra")

TLIM = [min(t), max(t)]

g1.set_xlim(TLIM)

g1.set_xlabel("Tempo [s]")

g1.set_ylabel("Ampiezza [digit]")

tra = numpy.fft.rfft(y)

tra = abs(tra)

print(len(tra))

f = numpy.linspace(0., 1., len(tra))
#poi vedi come mettere ma hai capito che devi usare abs(tra)

FLIM = [0., max(f)]

g2.set_xlim(FLIM)

g2.set_xlabel("Frequenza [Hz]")

g2.set_ylabel("Ampiezza [u.a.]")

pylab.errorbar(f, tra)

pylab.show()
