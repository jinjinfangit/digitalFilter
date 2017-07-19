# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:25:52 2017

@author: JFan
"""

#!python

from numpy import sin, arange, linspace, pi
from scipy.signal import lfilter
from scipy import signal
from NotchFilter import NotchFilter
from Utils import Utils
from PlotSignal import PlotSignal
from FilterConstant import FilterConstant

#------------------------------------------------
# Signal parameters
#------------------------------------------------


filename = input('Enter the directory where contains coefficients files:')
gain = int(input('Enter Gain:'))
lowcut = int(input('Enter low frequency:'))
highcut = int(input('Enter high frequency:'))
ffs = [10, highcut/2]  # frequencies of the signal

Ts = 1.0/FilterConstant.sample_rate
sineInterval = arange(0, 1 ,Ts) # time vector
# Create square wave parameters
squareInterval = linspace(0, 1, FilterConstant.sample_rate, endpoint=False)

#------------------------------------------------
# Dependant classes
#------------------------------------------------
util = Utils(gain, FilterConstant.sample_rate, FilterConstant.qfactor)
plotsignal = PlotSignal(gain, FilterConstant.sample_rate,
                        FilterConstant.qfactor, lowcut, highcut)

taps, taps_len = util.generateTaps(filename)

#------------------------------------------------
# Main starts here
#------------------------------------------------
# Plot the FIR filter coefficients and
# the magnitude response of the filter.
#------------------------------------------------
plotsignal.plotFilter(taps)

#------------------------------------------------
# Generate signals before and after
#------------------------------------------------
for ff in ffs:
    sineWave = sin(2*pi*ff*sineInterval)
    squareWave = signal.square(2 * pi * ff * squareInterval)
    filtered_sinewave = lfilter(taps, 1.0, sineWave)
    downsample_sinewave = util.generateDownsample(filtered_sinewave)
    plotsignal.plotSignal(sineWave, filtered_sinewave, sineInterval,
                          'Sine wave', ff, 0.5 * (taps_len-1) / FilterConstant.sample_rate)
    plotsignal.plotDownSampling(filtered_sinewave, downsample_sinewave)
