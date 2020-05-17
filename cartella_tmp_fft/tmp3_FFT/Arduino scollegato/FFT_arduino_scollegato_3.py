from LIB import *

x, z = pylab.loadtxt(".dati6.txt", unpack = True)
x = x / 1000000 #seconds

t1 = numpy.zeros(256)
y1 = numpy.zeros(256)
t2 = numpy.zeros(256)
y2 = numpy.zeros(256)
t3 = numpy.zeros(256)
y3 = numpy.zeros(256)
t4 = numpy.zeros(256)
y4 = numpy.zeros(256)
t5 = numpy.zeros(256)
y5 = numpy.zeros(256)
t6 = numpy.zeros(256)
y6 = numpy.zeros(256)
t7 = numpy.zeros(256)
y7 = numpy.zeros(256)
t8 = numpy.zeros(256)
y8 = numpy.zeros(256)

for i in range(256):
    t1[i] = x[i]
    y1[i] = z[i]

for i in range(256):
    t2[i] = x[256+i]
    y2[i] = z[256+i]

for i in range(256):
    t3[i] = x[256*2+i]
    y3[i] = z[256*2+i]

for i in range(256):
    t4[i] = x[256*3+i]
    y4[i] = z[256*3+i]

for i in range(256):
    t5[i] = x[256*4+i]
    y5[i] = z[256*4+i]

for i in range(256):
    t6[i] = x[256*5+i]
    y6[i] = z[256*5+i]

for i in range(256):
    t7[i] = x[256*6+i]
    y7[i] = z[256*6+i]

for i in range(256):
    t8[i] = x[256*7+i]
    y8[i] = z[256*7+i]


#t.sort()

pylab.errorbar(t1, y1, color = 'blue')
pylab.errorbar(t2, y2, color = 'black')
pylab.errorbar(t3, y3, color = 'red')
pylab.errorbar(t4, y4, color = 'grey')
pylab.errorbar(t5, y5, color = 'green')
pylab.errorbar(t6, y6, color = 'yellow')
pylab.errorbar(t7, y7, color = 'violet')
pylab.errorbar(t8, y8, color = 'orange')
pylab.show()
pylab.title("Acquisizione con ingresso scollegato")
pylab.xlim(min(t1)*1000000, max(t1)*1000000)
pylab.ylim(min(y1)-2., max(y1)+2.)
pylab.minorticks_on()
pylab.grid(color = "gray")
pylab.grid(b=True, which='major', color='#666666', linestyle='-')
pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)    
pylab.xlabel("Tempo [us]")
pylab.ylabel("d.d.p. [digit]")
pylab.errorbar(t1*1000000, y1, 1.+t1*0., 4+t1*0., color = 'black', marker = '.')
pylab.show()
dtime = (max(t1) - min(t1))/len(t1)

tra_complessa = numpy.fft.rfft(y1)

tra = abs(tra_complessa)

f = numpy.linspace(0., 1./(dtime * 2), len(tra))

TLIM = [min(t1), max(t1)]

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

pylab.title("FFT, acquisione con ingresso scollegato")

pylab.xlim(FLIM)

pylab.xlabel("Frequenza[Hz]")

pylab.minorticks_on()

pylab.grid(color = "gray")

pylab.grid(b=True, which='major', color='#666666', linestyle='-')

pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

pylab.ylabel("Ampiezza in dB")

#pylab.xlim(min(t1)*1000000, max(t1)*1000000)
#pylab.ylim(min(y1)-2., max(y1)+2.)
pylab.minorticks_on()
pylab.grid(color = "gray")
pylab.grid(b=True, which='major', color='#666666', linestyle='-')
pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)    

pylab.show() 

P = 0.

for i in range(len(tra)):
    if(i!=0) and (tra[i]>P):
        P = tra[i]
        F = f[i]

print(F)
        
deltaf = 1/(len(t1)*dtime)
print(deltaf)
fmax = 1./(dtime * 2)
print(fmax)
