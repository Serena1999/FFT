#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                             PROVA ERRORI                            #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
from LIB import *
import random
random.seed(2)

FileName = "quadra_50hz.txt"
Directory = "esp_6_da_quadra/"

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
    if(i == 999):
        pylab.errorbar(f, w, color = 'blue', label = 'cinque sigma')
    else:
        pylab.errorbar(f, w, color = 'blue')
    dtime = (max(t + b*4.*dt) - min(t + b*4.*dt))/len(t)
    w = abs(numpy.fft.rfft(y + a*4.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    if(i == 999):
        pylab.errorbar(f, w, color = 'green', label = 'quattro sigma')
    else:
        pylab.errorbar(f, w, color = 'green')
    dtime = (max(t + b*3.*dt) - min(t + b*3.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*3.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    if(i == 999):
        pylab.errorbar(f, w, color = 'yellow', label = 'tre sigma')
    else:
        pylab.errorbar(f, w, color = 'yellow')
    dtime = (max(t + b*2.*dt) - min(t + b*2.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*2.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    if(i == 999):
        pylab.errorbar(f, w, color = 'orange', label = 'due sigma')
    else:
        pylab.errorbar(f, w, color = 'orange')
    dtime = (max(t + b*1.*dt) - min(t + b*1.*dt))/len(t)
    f = numpy.linspace(0., 1./(dtime * 2), len(tra))
    w = abs(numpy.fft.rfft(y + a*1.*dy))#dopo vedi
    w = max(w)*20.*pylab.log(w/max(w))
    if(i == 999):
        pylab.errorbar(f, w, color = 'red', label = 'un sigma')
    else:
        pylab.errorbar(f, w, color = 'red')
    print(i)

pylab.minorticks_on()
pylab.grid(color = "gray")
pylab.grid(b=True, which='major', color='#666666', linestyle='-')
pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)    
dtime = (max(t) - min(t))/len(t)
f = numpy.linspace(0., 1./(dtime * 2), len(tra))
pylab.xlim(0., 1./(dtime * 2))
pylab.errorbar(f, tradB, color = 'black')
pylab.title("FFT con bande di confidenza")
pylab.xlabel("Frequenza [Hz]")
pylab.ylabel("Ampiezza in dB")
legend = pylab.legend(loc='upper right', shadow=True, fontsize='medium')
pylab.show()
