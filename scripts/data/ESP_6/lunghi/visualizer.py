#TO_VISUALIZE
import pylab
x, y= pylab.loadtxt('quadra_50hz.txt', unpack = True)
pylab.errorbar(x,y)
pylab.show()
