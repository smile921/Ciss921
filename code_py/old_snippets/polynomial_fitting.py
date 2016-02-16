# Polynomial Fitting

import scipy.interpolate as sp
import numpy
import pylab

# 50 points of sin(x) in [0 10]
xx = numpy.linspace(0, 10, 50)
yy = numpy.sin(xx)

# 10 sample of sin(x) in [0 10]
x = numpy.linspace(0, 10, 10)
y = numpy.sin(x)

# interpolation
fl = sp.interp1d(x, y,kind='linear')
fc = sp.interp1d(x, y,kind='cubic')

# fl and fc are the interpolating functions
# defined in the interval [0 10]
# fl uses linear interpolation
# and fc uses cubic interpolation

xnew = numpy.linspace(0, 10, 50)
pylab.subplot(211)
# the real sin(x) function plot
pylab.plot(xx, yy)
pylab.legend(['sin(x)'], loc='best')
pylab.subplot(212)
# the interpolation
pylab.plot(x, y, 'o', xnew, fl(xnew), xnew, fc(xnew))
pylab.legend(['sample', 'linear', 'cubic'], loc='lower left')
pylab.show()
