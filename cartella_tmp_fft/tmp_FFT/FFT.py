#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                           FFT TRANSFORM                             #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from CONFIG_vecchio import *

for Name in FileName1:

    print(Name)
    
    t, y = pylab.loadtxt(Directory1+Name, unpack = True)
    
    t = t / 1000000 #secondi

    dt = t * 0. + 4./ 1000000 #secondi

    dy = y * 0. + 1 #digit

    pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')

    pylab.show()

    gridsize = (3, 1)

    g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)

    g2 = plt.subplot2grid(gridsize,(2,0), colspan = 2)

    g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '', color = 'black')

    ##DA METTERE BENE g1.set_title("Onda quadra")

    TLIM = [min(t), max(t)]

    g1.set_xlim(TLIM)

    g1.set_xlabel("Tempo [s]")

    g1.set_ylabel("d.d.p. [digit]")

    tra = numpy.fft.rfft(y)

    tra = abs(tra)

    print(len(tra))

    dtime = (max(t) - min(t))/(len(t) - 1)

    print(dtime) #questo modifica con media e varianza

    f = numpy.linspace(0., 1./(dtime * 2), len(tra))

    FLIM = [0., max(f)]

    g2.set_xlim(FLIM)

    g2.set_xlabel("Frequenza [Hz]")

    g2.set_ylabel("Ampiezza [u.a.]")

    g2.errorbar(f, tra, linestyle = '-', color = 'black')

    pylab.semilogy()

    pylab.show()
    
    
    #il range di frequenza va da 0 a 1/(2dtime)


##smorzaverage riprendili dopo (4 elementi)
