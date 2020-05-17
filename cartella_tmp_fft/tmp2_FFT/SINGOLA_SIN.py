from LIB import *

bool_sinusoidale = True
FileNameSin1 = ["datilunghisinusoidale.txt"]
Directories = ["data_sinusoidale/"]
##poi in quello completo c'è da aggiungerci anche l'altro

##variabili booleane da aggiungere
bool_grafico_semplice_sin = False
bool_grafico_doppio_sin = False
bool_logartmica_sin = False
boll_decibel_sin = False
bool_filtro_sin = True ####NON MI FUNZIONANO I NUMERI COMPLESSI CONTROLLA, da finire
bool_finestra_sin = False ##controlla se hai fatto bene, ho fatto quella gaussiana
##comunque qui questa bool non sembra avere tanti effetti ma magari prova anche su altre,
##gli effetti di bordo si sentono poco
bool_grafici_singoli_FFT_sin = False
bool_grafici_singoli_FFTlog_sin = False
bool_grafici_singoli_FFTdB_sin = False
bool_grafici_focus_sin = False
bool_fit_sin = False

par_sin1 = [314, -1.57, 312, 360]

def f_sin(x, omega, phi, q, A):
    return A*pylab.sin(omega*x + phi) + q

def non_norm_Gauss(x, m, sigma):
    return pylab.exp((-(1/2)*((x - m)/sigma)**2))

def f_intGauss(x, m, sigma, estremoa, estremob):
    a = numpy.linspace(estremoa, estremob, 100000)
    for l in range(len(a)):
        a[l] = non_norm_Gauss(a[l], m, sigma)
    C = a.sum()
    return C

def f_Gauss(x, m, sigma, C):
    return non_norm_Gauss(x, m, sigma)/C

sigma0 = 0.1 ##modifica con minori di 0.5 per vedere che succese
##

if(bool_sinusoidale):
    print("\n FFT SINUSOIDALE:\n")
    for Name in FileNameSin1:
        print(Name)
        t, y = pylab.loadtxt(Directories[0]+Name, unpack = True)
        t = t / 1000000 #secondi
        dt = t * 0. + 4./ 1000000 #secondi
        dy = y * 0. + 1 #digit
        dtime = (max(t) - min(t))/len(t) ##questa cosa controllala meglio
        C_NORMAL =  f_intGauss(t, (max(t) - min(t))/2., sigma0, min(t), max(t))
        if(bool_finestra_sin):
            y_fin = numpy.zeros(len(y))
            for i in range(len(y)):
                y_fin[i] = y[i] *f_Gauss(t[i], (max(t) - min(t))/2, sigma0, C_NORMAL) 
            tra_complessa = numpy.fft.rfft(y_fin)
        else:
            tra_complessa = numpy.fft.rfft(y)
        tra = abs(tra_complessa)
        f = numpy.linspace(0., 1./(dtime * 2), len(tra))
        TLIM = [min(t), max(t)]
        FLIM = [0., max(f)]
        tradB = max(tra)*20*pylab.log(tra/max(tra))##controlla meglio che non sono sicura... comunque è bellissimo
        if(bool_grafico_semplice_sin):
            pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
            pylab.show()
        if(bool_grafico_doppio_sin):
            gridsize = (4, 1)
            g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
            g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
            g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '', color = 'black')
            g1.set_title("Onda sinusoidale")
            g2.set_title("FFT")
            g1.set_xlim(TLIM)
            g1.set_xlabel("Tempo [s]")
            g1.set_ylabel("d.d.p. [digit]")
            g2.set_xlim(FLIM)
            g2.set_xlabel("Frequenza [Hz]")
            if(boll_decibel_sin):
                g2.set_ylabel("Ampiezza in dB[u.a]")
            else:
                g2.set_ylabel("Ampiezza [u.a.]")
            if(boll_decibel_sin):
                g2.errorbar(f, tradB, linestyle = '-', color = 'black')
            else:
                g2.errorbar(f, tra, linestyle = '-', color = 'black')
            pylab.show()
            if (bool_logartmica_sin):
                gridsize = (4, 1)
                g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
                g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
                g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '', color = 'black')
                g1.set_title("Onda sinusoidale")
                g2.set_title("FFT")
                g1.set_xlim(TLIM)
                g1.set_xlabel("Tempo [s]")
                g1.set_ylabel("d.d.p. [digit]")
                g2.set_xlim(FLIM)
                g2.set_xlabel("Frequenza [Hz]")
                g2.set_ylabel("Ampiezza [u.a.]")
                g2.errorbar(f, tra, linestyle = '-', color = 'black')
                g2.semilogy()
                pylab.show()
        if(bool_grafici_singoli_FFT_sin or bool_grafici_singoli_FFTlog_sin or bool_grafici_singoli_FFTdB_sin):
            pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '', color = 'black')
            pylab.title("Onda sinusoidale")
            pylab.xlim(TLIM)
            pylab.xlabel("Tempo [s]")
            pylab.ylabel("d.d.p. [digit]")
            pylab.show()
        if(bool_grafici_singoli_FFT_sin):            
            pylab.errorbar(f, tra, linestyle = '-', color = 'black')
            pylab.title("FFT Onda sinusoidale")
            if((bool_grafici_focus_sin) and (Name == "datilunghisinusoidale.txt")):
                pylab.xlim(0., 100.)
            else:
                pylab.xlim(FLIM)
            pylab.xlabel("Frequenza [Hz]")
            pylab.ylabel("Ampiezza [u.a]")
            pylab.show()
        if(bool_grafici_singoli_FFTlog_sin):
            pylab.errorbar(f, tra, linestyle = '-', color = 'black')
            pylab.title("FFT Onda sinusoidale")
            if((bool_grafici_focus_sin) and (Name == "datilunghisinusoidale.txt")):
                pylab.xlim(0., 100.)
            else:
                pylab.xlim(FLIM)
            pylab.xlabel("Frequenza [Hz]")
            pylab.ylabel("Ampiezza [u.a]")
            pylab.semilogy()
            pylab.show()
        if(bool_grafici_singoli_FFTdB_sin):
            pylab.errorbar(f, tradB, linestyle = '-', color = 'black')
            pylab.title("FFT Onda sinusoidale")
            if((bool_grafici_focus_sin) and (Name == "datilunghisinusoidale.txt")):
                pylab.xlim(0., 100.)
            else:
                pylab.xlim(FLIM)
            pylab.xlabel("Frequenza [Hz]")
            pylab.ylabel("Ampiezza in dB [u.a]")
            pylab.show()
        if((bool_fit_sin) and (Name == "datilunghisinusoidale.txt")):
            popt, pcov = curve_fit(f_sin, t, y, par_sin1, dy, absolute_sigma = False)
            omega0, phi0, q0, A0 = popt
            domega0, dphi0, dq0, dA0 = pylab.sqrt(pcov.diagonal())
            dw = numpy.zeros(len(t))
            for n in range(10):
                for i in range(len(t)):
                    dw[i] = pylab.sqrt((dy[i])**2 + (A0*omega0*dt[i]*pylab.cos(omega0*t[i]))**2)
                print(dw)
                popt, pcov = curve_fit(f_sin, t, y, [omega0, phi0, q0, A0], dw, absolute_sigma = False)
                omega0, phi0, q0, A0 = popt
                domega0, dphi0, dq0, dA0 = pylab.sqrt(pcov.diagonal())                
            print("omega = %f +- %f" %(omega0, domega0))
            print("phi = %f +- %f" %(phi0, dphi0))
            print("q = %f +- %f" %(q0, dq0))
            print("A = %f +- %f" %(A0, dA0))
            pylab.errorbar(t, y, linestyle = '-', color = 'black')
            pylab.title("Onda sinusoidale")
            pylab.xlim(TLIM)
            pylab.xlabel("Tempo [s]")
            pylab.ylabel("d.d.p. [digit]")
            x_plot = numpy.linspace(*TLIM, 1000)
            pylab.plot(x_plot, f_sin(x_plot, *popt), color = "red")
            print("Quindi f aspettata è %f " %(omega0/(2*pylab.pi)))
            pylab.show()
#50 hz

##PARTE MOMENTANEA

def passa_basso(w):
    return 1./(1. + w*1j/100)

def passa_alto(w):##controlla (ma dovrebbe essere col meno)
    return 1./(1. - 20j/w)


if(bool_sinusoidale):
    print("\n FFT SINUSOIDALE:\n")
    for Name in FileNameSin1:
        print(Name)
        t, y = pylab.loadtxt(Directories[0]+Name, unpack = True)
        t = t / 1000000 #secondi
        dt = t * 0. + 4./ 1000000 #secondi
        dy = y * 0. + 1 #digit
        dtime = (max(t) - min(t))/len(t) ##questa cosa controllala meglio
        C_NORMAL =  f_intGauss(t, (max(t) - min(t))/2., sigma0, min(t), max(t))
        if(bool_finestra_sin):
            y_fin = numpy.zeros(len(y))
            for i in range(len(y)):
                y_fin[i] = y[i] *f_Gauss(t[i], (max(t) - min(t))/2, sigma0, C_NORMAL) 
            tra_complessa = numpy.fft.rfft(y_fin)
        else:
            tra_complessa = numpy.fft.rfft(y)
        tra = abs(tra_complessa)
        f = numpy.linspace(0., 1./(dtime * 2), len(tra))
        TLIM = [min(t), max(t)]
        FLIM = [0., max(f)]
        tradB = max(tra)*20*pylab.log(tra/max(tra))##controlla meglio che non sono sicura... comunque è bellissimo
        if(bool_filtro_sin):
        #    coeff = 0.
        #    for k in range(len(f)):
        #        if((tra[k] >= coeff) and (f[k]!= 0)):
        #            coeff = f[k]
        #    print(coeff)
            gomegaout = numpy.zeros(len(f), dtype = complex)
            for i in range(len(f)):
                if(f[i] == 0):
                    gomegaout[i] = tra[i]
                else:
                    a = passa_basso(f[i])
                    gomegaout[i] = a.real * tra_complessa[i].real -a.imag * tra_complessa[i].imag
                    gomegaout[i] = gomegaout[i] + 1j * (a.imag + tra_complessa[i].imag)
                    #gomegaout[i] = passa_basso(f[i]) * tra_complessa[i]
            ampiezza_t = abs(numpy.fft.irfft(gomegaout))
            pylab.errorbar(t, ampiezza_t)
            pylab.show()
            new_tra = abs(numpy.fft.rfft(ampiezza_t))
            pylab.errorbar(f, new_tra)
            pylab.show()
            new_tra_dB = max(new_tra)*20*pylab.log(new_tra/max(new_tra))
            pylab.errorbar(f, new_tra_dB)
            pylab.show()
