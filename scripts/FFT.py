#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                                FFT                                  #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

from FUNCTIONS import *

#A = ampiezza
#t = tempo
t, A = pylab.loadtxt("data/ESP_5/datilunghiquadra.txt", unpack = True)

gridsize = (3, 1)
g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
g2 = plt.subplot2grid(gridsize,(2,0), colspan = 2)

g1.errorbar(t, A, linestyle = '', marker = '.', color = 'red')
pylab.minorticks_on()
pylab.show()
