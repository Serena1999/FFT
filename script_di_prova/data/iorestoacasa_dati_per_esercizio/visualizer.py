#TO_VISUALIZE
import pylab
x,y= pylab.loadtxt('transosc15.txt', unpack = True)
pylab.errorbar(x,y)
pylab.show()
