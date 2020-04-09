from LIB import *

#nota converti in secondi

##onda quadra

Directory = "data/ESP_5/"

FileName = "datilunghiquadra.txt"

##onda sinusoidale

#Directory = "data/ESP_5/"

#FileName = "datilunghisinusoidale.txt"

##onda triangolare

#Directory = "data/ESP_5/"

#FileName = "datilunghitriangolare.txt"

##onda sinusoidale più corta

#Directory = "data/ESP_5/"

#FileName = "datiardu_001.txt"

##

#Directory = "data/ESP_5/"

#FileName = "datiardu.txt"

##

#Directory = "data/iorestoacasa_dati_per_esercizio/"

#FileName = "sin11.txt"

##

#Directory = "data/iorestoacasa_dati_per_esercizio/"

#FileName = "smorz1.txt"


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

g2.errorbar(f, tra)

pylab.show()

dtime = (max(t) - min(t))/(len(t) - 1)

print(dtime)

#il range di frequenza va da 0 a 1/(2dtime)

frequency = numpy.linspace(0., 1./(dtime * 2), len(tra))

pylab.errorbar(frequency, tra)

pylab.semilogy()

pylab.show()

#4.76*10^(-5) -> T = 2* 10^4---30515-679 = Ttipo va bastante bien!
