#TO_VISUALIZE
import pylab
x, y= pylab.loadtxt('200hz.txt', unpack = True)
pylab.errorbar(x,y)
pylab.show()
