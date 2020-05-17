from LIB import *

t, y = pylab.loadtxt(".dati6.txt", unpack = True)
t = t / 1000000 #seconds


for i in range(len(t)):
    M = t[i]
    index = i
    for j in range(i+1, len(t)):
        if(t[j]<M):
            M = t[j]
            index = j
    t[index] = t[i]
    S = y[index]
    y[index] = y[i]
    t[i] = M
    y[i] = S

#t.sort()

pylab.errorbar(t, y)

pylab.show()

dtime = (max(t) - min(t))/len(t)

tra_complessa = numpy.fft.rfft(y)

tra = abs(tra_complessa)

f = numpy.linspace(0., 1./(dtime * 2), len(tra))

TLIM = [min(t), max(t)]

FLIM = [0., max(f)]

tradB = max(tra)*20*pylab.log(tra/max(tra))

pylab.errorbar(f, tra, linestyle = '-', color = 'black')

pylab.title("FFT") #cambia

pylab.xlim(FLIM)

pylab.xlabel("Frequenza [Hz]")

pylab.minorticks_on()

pylab.grid(color = "gray")

pylab.grid(b=True, which='major', color='#666666', linestyle='-')

pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

pylab.ylabel("Ampiezza [u.a.]")

pylab.show()

pylab.errorbar(f, tradB, linestyle = '-', color = 'black')

pylab.title("FFT onda sinusoidale")

pylab.xlim(FLIM)

pylab.xlabel("Frequenza [Hz]")

pylab.minorticks_on()

pylab.grid(color = "gray")

pylab.grid(b=True, which='major', color='#666666', linestyle='-')

pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

pylab.ylabel("Ampiezza [u.a.]")

pylab.show() 

P = 0.

for i in range(len(tra)):
    if(i!=0) and (tra[i]>P):
        P = tra[i]
        F = f[i]

print(F)
        
