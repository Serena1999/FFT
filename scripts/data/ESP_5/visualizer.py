#TO_VISUALIZE
import pylab
x, y= pylab.loadtxt('datiardu.txt', unpack = True)
pylab.errorbar(x,y)
pylab.show()
