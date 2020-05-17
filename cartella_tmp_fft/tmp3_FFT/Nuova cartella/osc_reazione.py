#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                           SINGLE SINUSOIDALE                        #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
from LIB import *



#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                                CONFIG                               #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
# --> choosen file::
FileName = "transosc01.txt"
Directory = "data_osc_reazione_F/"

# --> fit  initial parameters::
par_sin1 = [628, -1.57, 214, 198]#per fit

# --> weight of edge::
# [it is used to set the weight of the edge (it is the standard deviation of a
#  Gaussian distribution that multiplies the array in input in the FFT)]
sigma0 = 0.3 ##change with numbers that are lower than 0.5 to see what happens

# --> wt_high = cutoff frequency of high-pass filter
# --> wt_low = cutoff frequency of low-pass filter
wt_high = 5
wt_low = 100

# --> TFOCUS = the edge of the array of frequency to focus on if
#bool_focus_FFT = True
FFOCUS = [0., 400.]

# -->boolean variables::
# [bool_single_time = True to visualize the function of time only]
bool_single_time = True
# [bool_single_FFT = True to visualize the FFT only]
bool_single_FFT = True
# [bool_double_graph = True to visualize the function of the time and of the
#  frequency together]
bool_double_graph = True
# [bool_lin = True to visualize the FFT (linear scale: y)]
bool_lin = True
# [bool_log = True to visualize the FFT with pylab.semilogy()]
bool_log = True
# [bool_dB = True to viualize the FFT in dB]
bool_dB = True
# [bool_filter_low = True to use the Low Pass Filter]
bool_filter_low = True
# [bool_filter_high = True to use the High Pass Filter]
bool_filter_high = True
# [bool_focus_FFT = True to show only a part of frequencies]
bool_focus_FFT = False
# [bool_window = True to use a Window to give a weight to the input array in
# FFT]
bool_window = True
# [bool_fit = True to do the best fit]
bool_fit = True##CONTROLLA O MAGARI PROVA CON ALTRI FILE

#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                             FUNCTIONS                               #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

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

def low_filter(w):
    return 1./(1. + w*1j/wt_low)

def high_filter(w):
    return 1./(1. - wt_high*1j/w)


#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#                            PROCEEDING                               #
#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
t, y = pylab.loadtxt(Directory+FileName, unpack = True)
t = t / 1000000 #seconds
dt = t * 0. + 4./ 1000000 #seconds
dy = y * 0. + 1 #digit
dtime = (max(t) - min(t))/len(t)
C_NORMAL =  f_intGauss(t, (max(t) - min(t))/2., sigma0, min(t), max(t))
if(bool_window):
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
tradB = max(tra)*20*pylab.log(tra/max(tra))
if(bool_double_graph):
    if(bool_lin):
        gridsize = (4, 1)
        g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
        g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
        g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
        g1.set_title("Onda sinusoidale")
        g2.set_title("FFT")
        g1.grid(color = "gray")
        g1.grid(b=True, which='major', color='#666666', linestyle='-')
        g1.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g2.grid(color = "gray")
        g2.grid(b=True, which='major', color='#666666', linestyle='-')
        g2.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g1.set_xlim(TLIM)
        g1.set_xlabel("Tempo [s]")
        g1.set_ylabel("d.d.p. [digit]")
        if(bool_focus_FFT):
            g2.set_xlim(FFOCUS)
        else:
            g2.set_xlim(FLIM)
        g2.set_xlabel("Frequenza [Hz]")
        g2.set_ylabel("Ampiezza [u.a.]")
        g1.minorticks_on()
        g2.minorticks_on()
        g2.errorbar(f, tra, linestyle = '-', color = 'black')
        pylab.show()
    if(bool_log):
        gridsize = (4, 1)
        g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
        g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
        g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
        g1.set_title("Onda sinusoidale")
        g2.set_title("FFT")
        g1.set_xlim(TLIM)
        g1.set_xlabel("Tempo [s]")
        g1.set_ylabel("d.d.p. [digit]")
        if(bool_focus_FFT):
            g2.set_xlim(FFOCUS)
        else:
            g2.set_xlim(FLIM)
        g2.set_xlabel("Frequenza [Hz]")
        g2.set_ylabel("Ampiezza [u.a.]")
        g2.errorbar(f, tra, linestyle = '-', color = 'black')
        g1.minorticks_on()
        g2.minorticks_on()
        g1.grid(color = "gray")
        g1.grid(b=True, which='major', color='#666666', linestyle='-')
        g1.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g2.grid(color = "gray")
        g2.grid(b=True, which='major', color='#666666', linestyle='-')
        g2.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g2.semilogy()
        pylab.show()
    if(bool_dB):
        gridsize = (4, 1)
        g1 = plt.subplot2grid(gridsize,(0,0),colspan = 1, rowspan = 2)
        g2 = plt.subplot2grid(gridsize,(3,0), colspan = 2)
        g1.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
        g1.set_title("Onda sinusoidale")
        g2.set_title("FFT")
        g1.set_xlim(TLIM)
        g1.set_xlabel("Tempo [s]")
        g1.set_ylabel("d.d.p. [digit]")
        if(bool_focus_FFT):
            g2.set_xlim(FFOCUS)
        else:
            g2.set_xlim(FLIM)
        g2.set_xlabel("Frequenza [Hz]")
        g2.set_ylabel("Ampiezza [u.a.]")
        g1.minorticks_on()
        g2.minorticks_on()
        g1.grid(color = "gray")
        g1.grid(b=True, which='major', color='#666666', linestyle='-')
        g1.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g2.grid(color = "gray")
        g2.grid(b=True, which='major', color='#666666', linestyle='-')
        g2.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        g2.errorbar(f, tradB, linestyle = '-', color = 'black')
        pylab.show()            
if(bool_single_time):
    pylab.errorbar(t, y, dy, dt, marker = '.', linestyle = '-', color = 'black')
    pylab.title("Onda sinusoidale")
    pylab.xlim(TLIM)
    pylab.minorticks_on()
    pylab.grid(color = "gray")
    pylab.grid(b=True, which='major', color='#666666', linestyle='-')
    pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)    
    pylab.xlabel("Tempo [s]")
    pylab.ylabel("d.d.p. [digit]")
    pylab.show()
if(bool_single_FFT):
    if(bool_lin):
        pylab.errorbar(f, tra, linestyle = '-', color = 'black')
        pylab.title("FFT onda sinusoidale")
        if(bool_focus_FFT):
            pylab.xlim(FFOCUS)
        else:
            pylab.xlim(FLIM)
        pylab.xlabel("Frequenza [Hz]")
        pylab.minorticks_on()
        pylab.grid(color = "gray")
        pylab.grid(b=True, which='major', color='#666666', linestyle='-')
        pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        pylab.ylabel("Ampiezza [u.a.]")
        pylab.show()       
    if(bool_log):
        pylab.errorbar(f, tra, linestyle = '-', color = 'black')
        pylab.title("FFT onda sinusoidale")
        if(bool_focus_FFT):
            pylab.xlim(FFOCUS)
        else:
            pylab.xlim(FLIM)
        pylab.xlabel("Frequenza [Hz]")
        pylab.minorticks_on()
        pylab.grid(color = "gray")
        pylab.grid(b=True, which='major', color='#666666', linestyle='-')
        pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        pylab.ylabel("Ampiezza [u.a.]")
        pylab.semilogy()
        pylab.show()               
    if(bool_dB):
        pylab.errorbar(f, tradB, linestyle = '-', color = 'black')
        pylab.title("FFT onda sinusoidale")
        if(bool_focus_FFT):
            pylab.xlim(FFOCUS)
        else:
            pylab.xlim(FLIM)
        pylab.xlabel("Frequenza [Hz]")
        pylab.minorticks_on()
        pylab.grid(color = "gray")
        pylab.grid(b=True, which='major', color='#666666', linestyle='-')
        pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
        pylab.ylabel("Ampiezza [u.a.]")
        pylab.show() 
if(bool_fit):##mancano residui
    popt, pcov = curve_fit(f_sin, t, y, par_sin1, dy, absolute_sigma = False)
    omega0, phi0, q0, A0 = popt
    domega0, dphi0, dq0, dA0 = pylab.sqrt(pcov.diagonal())
    dw = numpy.zeros(len(t))
    for n in range(10):
        for i in range(len(t)):
            dw[i] = pylab.sqrt((dy[i])**2 + (A0*omega0*dt[i]*pylab.cos(omega0*t[i]))**2)
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
    pylab.minorticks_on()
    pylab.grid(color = "gray")
    pylab.grid(b=True, which='major', color='#666666', linestyle='-')
    pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    print("Quindi f aspettata è %f " %(omega0/(2*pylab.pi)))
    pylab.show()
if(bool_filter_low):
    coeff = -1000.
    for i in range(len(tra)):
        if((tra[i] > coeff) and (f[i] != 0)):
            coeff = tra[i]
            coeff_f = f[i]
    print("La w aspettata per la sinusoide è %f" %coeff_f)
    gfilter = numpy.zeros(len(f), dtype = complex)
    for i in range(len(f)):
        if(f[i] == 0):
            gfilter[i] = tra[i]
        else:
            gfilter[i] = low_filter(f[i]) * tra_complessa[i]
    ampiezza_t = abs(numpy.fft.irfft(gfilter))
    pylab.errorbar(t, ampiezza_t, marker = '.', color = 'black')
    pylab.show()
    C_NORMAL =  f_intGauss(ampiezza_t, (max(ampiezza_t) - min(ampiezza_t))/2., sigma0, min(ampiezza_t), max(ampiezza_t))
    if(bool_window):
        y_fin = numpy.zeros(len(ampiezza_t))
        for i in range(len(ampiezza_t)):
            y_fin[i] = ampiezza_t[i] *f_Gauss(ampiezza_t[i], (max(ampiezza_t) - min(ampiezza_t))/2, sigma0, C_NORMAL) 
            new_tra = abs(numpy.fft.rfft(y_fin))
    else:
        new_tra = abs(numpy.fft.rfft(ampiezza_t))
    pylab.errorbar(f, new_tra, color = 'black')
    pylab.minorticks_on()
    pylab.grid(color = "gray")
    pylab.grid(b=True, which='major', color='#666666', linestyle='-')
    pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    pylab.show()
    pylab.grid(color = "gray")
    pylab.grid(b=True, which='major', color='#666666', linestyle='-')
    pylab.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    pylab.minorticks_on()
    new_tra_dB = max(new_tra)*20*pylab.log(new_tra/max(new_tra))
    pylab.errorbar(f, new_tra_dB, color = 'black')
    pylab.show()

##metti griglie, titoli, qualche didascalia se serve
##fai stmpare info utili, guarda lezione sbobinata
##vedi se riesci a metterci una banda d'errore in modo analitico:
##pensavo di fare random 10000 fft con valori entro le incertezze
##e fare una sorta di nuvola di densità a cui sovrapporre la mia funzione
