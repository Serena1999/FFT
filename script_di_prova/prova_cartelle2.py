from prova_cartelle import *

Directory = "data/iorestoacasa_dati_per_esercizio/"

for Name in FileName[0]:
    print(Name)
    t, y = pylab.loadtxt(Directory+Name, unpack = True)
    t = t/1000 #secondi
    dt = t * 0. + 4. /1000#secondi
    dy = y * 0. + 1 #digit
    pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
    pylab.show()
##continua a sistemare
