#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                          FFT ONDA TRIANGOLARE                       #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
from FFT_QUADRA import *

if(bool_triangolare):
    print("\n FFT ONDA TRIANGOLARE:\n")
    for Name in FileNameTria:
        print(Name)
        t, y = pylab.loadtxt(Directories[7]+Name, unpack = True)
        t = t / 1000000 #secondi
        dt = t * 0. + 4./ 1000000 #secondi
        dy = y * 0. + 1 #digit
        pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
        pylab.show()
        gridsize = (4, 1)
        g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
        g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
        g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
        g1.set_title("Onda triangolare")
        g2.set_title("FFT")
        TLIM = [min(t), max(t)]
        g1.set_xlim(TLIM)
        g1.set_xlabel("Tempo [s]")
        g1.set_ylabel("d.d.p. [digit]")
        tra = numpy.fft.rfft(y)
        tra = abs(tra)
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
#FFT_TRIANGLE

