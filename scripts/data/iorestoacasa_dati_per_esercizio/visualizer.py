#TO_VISUALIZE
import pylab
x,dx, y, dy= pylab.loadtxt('smorzaverage30.txt', unpack = True)
pylab.errorbar(x,y, dy, dx)
pylab.show()
