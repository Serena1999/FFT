#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                             PROVA ERRORI                            #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
from LIB import *
import random
random.seed(2)

FileName = "datilunghisinusoidale.txt"
Directory = "data_sinusoidale/"

t, y = pylab.loadtxt(Directory+FileName, unpack = True)
t = t / 1000000 #seconds
dt = t * 0. + 4./ 1000000 #seconds
dy = y * 0. + 1 #digit
tra_complessa = numpy.fft.rfft(y)
tra = abs(tra_complessa)
TLIM = [min(t), max(t)]
tradB = max(tra)*20*pylab.log(tra/max(tra))


a = numpy.zeros(len(t))
b = numpy.zeros(len(t))
for i in range(1000):
    for j in range(len(t)):
        a[j] = random.uniform(-1., 1.)
    for j in range(len(t)):
        b[j] = random.uniform(-1., 1.)    
    dtime = (max(t + b*5.*dt) - min(t + b*5.*dt))/len(t)
    w = abs(numpy.fft.rfft(y + a*5.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    pylab.errorbar(f, w, color = 'blue')
    dtime = (max(t + b*4.*dt) - min(t + b*4.*dt))/len(t)
    w = abs(numpy.fft.rfft(y + a*4.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    pylab.errorbar(f, w, color = 'green')
    dtime = (max(t + b*3.*dt) - min(t + b*3.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*3.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    pylab.errorbar(f, w, color = 'yellow')
    dtime = (max(t + b*2.*dt) - min(t + b*2.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*2.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    pylab.errorbar(f, w, color = 'orange')
    dtime = (max(t + b*1.*dt) - min(t + b*1.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*1.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    pylab.errorbar(f, w, color = 'red')
    print(i)

dtime = (max(t) - min(t))/len(t)
f = numpy.linspace(0., 1./(dtime * 2), len(tra))
pylab.errorbar(f, tradB, color = 'black')

pylab.show()
