# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:25:52 2017

@author: JFan
"""

#!python

from numpy import sin, pi, absolute, arange, linspace, sqrt
from scipy.signal import lfilter, freqz
from pylab import figure, plot, xlabel, ylabel, ylim, title, grid, show, subplot, subplots_adjust
import matplotlib.pyplot as plt
from matplotlib import gridspec
from scipy import fft, signal

#------------------------------------------------
# Digtal filter parameters
#------------------------------------------------
GAIN = 0
lowcut = 0
highcut = 0

#------------------------------------------------
# Signal parameters
#------------------------------------------------
sample_rate = 0  # sampling rate

def plotSpectrum(ax, y, Fs, color):
    """
    Plots a Single-Sided Amplitude Spectrum of y(t)
    """
    n = len(y) # length of the signal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(int(n/2))] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(int(n/2))]
    ax.plot(frq, abs(Y), color) # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('Gain')

def plotSignal(before, after, interval, title, freq):
    #------------------------------------------------------
    # Plot the original and filtered sine signals
    #------------------------------------------------------
    delay = 0.5 * (4-1) / sample_rate
    # Plot in time domain
    fig = figure(2)
    gs = gridspec.GridSpec(2, 2)
    ax1 = fig.add_subplot(gs[:,0])
    ax1.plot(interval, before)
    # Plot the filtered signal, shifted to compensate for the phase delay.
    ax1.plot(interval-delay, after, 'r-')
    plt.xlabel('time (s)')
    plt.ylabel('Gain')
    plt.title('Gain vs time')
    plt.grid(True)
    plt.xlim(0, 1)
    grid(True)

    # Plot spectrum
    ax2 = fig.add_subplot(gs[0,1])
    plotSpectrum(ax2, before, sample_rate, 'b')
    plt.title('Gain vs Freq(before)')
    ax3 = fig.add_subplot(gs[1,1])
    plotSpectrum(ax3, after, sample_rate ,'r')
    plt.title('Gain vs Freq(after)')
    gs.update(wspace=0.5, hspace=0.5)
    plt.suptitle('IIR %s(%dHz)' %(title,freq))
    show()

#------------------------------------------------
# Main starts here
#------------------------------------------------
GAIN = int(input('Enter Gain:'))
lowcut = int(input('Enter low frequency:'))
highcut = int(input('Enter high frequency:'))
sample_rate = int(input('Enter sample rate:'))

ffs = [10, 100, 1000]  # frequencies of the signal
if lowcut > 0 :
    ffs.append(lowcut)
if lowcut + highcut > 1 :
    ffs.append((lowcut + highcut)/2)
ffs.append(highcut)
if highcut/2 > 1:
    ffs.append(highcut/2)# frequencies of the signal

#------------------------------------------------
# Signal parameters
#------------------------------------------------
# Create sine wave parameters
Ts = 1.0/sample_rate
sineInterval = arange(0, 1 ,Ts) # time vector
# Create square wave parameters
squareInterval = linspace(0, 1, sample_rate, endpoint=False)
# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.0

#------------------------------------------------
# Create a IIR filter
#------------------------------------------------

#3 Pole Adj Gauss LPF
b = [5.678524821710300150E-9,
1.703557446513090490E-8,
1.703557446513090490E-8,
5.678524821710300150E-9
]
a = [1.000000000000000000E0,
-2.992165429719710450E0,
2.984359105193572060E0,
-9.921936300456629000E-1]

#------------------------------------------------
# Plot the IIR filter coefficients and
# the magnitude response of the filter.
#------------------------------------------------
figure(1)
w, h = signal.freqz(b, a, 8000)
plt.plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
plt.plot([0, 0.5 * sample_rate], [GAIN * sqrt(0.5),GAIN * sqrt(0.5)],'--')
xlabel('Frequency (Hz)')
ylabel('Gain')
title('Frequency Response')
ylim(-0.05, 1.5*GAIN)
grid(True)
subplots_adjust(hspace=.5)

#------------------------------------------------
# Generate signals before and after
#------------------------------------------------
squareWave = signal.square(2 * pi * ffs[0] * squareInterval)
filtered_squarewave = lfilter(b, a, squareWave)
plotSignal(squareWave, filtered_squarewave, squareInterval, 'Square wave', ffs[0])

for ff in ffs:
    sineWave = sin(2*pi*ff*sineInterval)
    filtered_sinewave = lfilter(b, a, sineWave)
    plotSignal(sineWave, filtered_sinewave, sineInterval, 'Sine wave', ff)
