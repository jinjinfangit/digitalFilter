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
from RmsFilter import RmsFilter
#------------------------------------------------
# Signal parameters
#------------------------------------------------


filename = input('Enter the directory where contains coefficients files:')
gain = int(input('Enter Gain:'))
lowcut = int(input('Enter low frequency:'))
highcut = int(input('Enter high frequency:'))
ffs = [10, 100, 1000]  # frequencies of the signal

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
rmsFilter = RmsFilter(FilterConstant.sample_rate, FilterConstant.window_size)

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
    #Generate filter signals
    filtered_sinewave = lfilter(taps, 1.0, sineWave)
    plotsignal.plotSignal(sineWave, filtered_sinewave, sineInterval,
                          'Sine wave', ff, 0.5 * (taps_len-1) / FilterConstant.sample_rate)
    #Generate downsampling signals
    downsample_sinewave = util.generateDownsample(filtered_sinewave)
    plotsignal.plotDownSampling(filtered_sinewave, downsample_sinewave)

    #Generate RMS window signals
    rms_signal = rmsFilter.filter(filtered_sinewave)
    plotsignal.plotRMSWindow(filtered_sinewave, rms_signal, FilterConstant.window_size)
    #Generate upsampling signals
    lfactor = 4
    upsample_sinwave= util.generateUpsample(filtered_sinewave, lfactor)
    plotsignal.plotUpSampling(filtered_sinewave, upsample_sinwave, lfactor)
    lfactor = 32
    upsample_sinwave1 = util.generateUpsample(filtered_sinewave, lfactor)
    plotsignal.plotUpSampling(filtered_sinewave, upsample_sinwave1, lfactor)
