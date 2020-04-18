#TO_VISUALIZE
import pylab
x, y= pylab.loadtxt('200.txt', unpack = True)
pylab.errorbar(x,y)
pylab.show()
