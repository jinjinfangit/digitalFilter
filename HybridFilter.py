# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:25:52 2017

@author: JFan
"""

#!python

from numpy import sin, pi, absolute, arange, linspace, sqrt
from scipy.signal import lfilter, freqz, bode
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


def generateTaps(filename):
    floats = []
    with open(filename) as f:
        for line in f:
            floats.extend([float(number)* GAIN for number in line.split()])
    f.close()
    return floats

def plotSignal(before, after, interval, title, freq):
    #------------------------------------------------------
    # Plot the original and filtered sine signals
    #------------------------------------------------------
    delay = 0.5 * (N-1) / sample_rate
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
    plt.suptitle('FIR %s(%dHz)' %(title,freq))
    show()

#------------------------------------------------
# Main starts here
#------------------------------------------------
filename = input('Enter the filename which contains coefficients:')
GAIN = int(input('Enter Gain:'))
lowcut = 1 #int(input('Enter low frequency:'))
highcut = 64 #int(input('Enter high frequency:'))
sample_rate = 2048 #int(input('Enter sample rate:'))
"""
ffs = [10, 0.5, 100, 1000]  # frequencies of the signal
if lowcut > 0 :
    ffs.append(lowcut)
if lowcut + highcut > 1 :
    ffs.append((lowcut + highcut)/2)
ffs.append(highcut)
#ffs = [highcut/2]  # frequencies of the signal
"""
ffs = [10,1, 50, 60,highcut,100, 1000]

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
# Create a FIR filter
#------------------------------------------------
taps = generateTaps(filename)
N = len(taps)
#------------------------------------------------
# Plot the FIR filter coefficients and
# the magnitude response of the filter.
#------------------------------------------------
figure(1)
subplot(2,1,1)
plot(taps, 'bo-', linewidth=2)
title('Filter Coefficients (%d taps)' % N)
grid(True)
subplot(2,1,2)
# First plot the desired ideal response as a green(ish) rectangle.
rect = plt.Rectangle((lowcut, 0), highcut - lowcut, 1.0 * GAIN,
                     facecolor="#60ff60", alpha=0.2)
plt.gca().add_patch(rect)
# Plot the frequency response of each filter
w, h = freqz(taps, worN=8000)
plt.plot((w/pi)*nyq_rate, absolute(h), linewidth=2)
plt.plot([0, 0.5 * sample_rate], [GAIN*sqrt(0.5), GAIN* sqrt(0.5)],'--')
xlabel('Frequency (Hz)')
ylabel('Gain')
title('Frequency Response')
ylim(-0.05, 1.5 * GAIN)
grid(True)
subplots_adjust(hspace=.5)

numeratorLPF64HZ = [1.887315455600753420E-3,
5.661946366802261820E-3,
5.661946366802261820E-3,
1.887315455600753420E-3]

denominatorLPF64HZ = [1.000000000000000000E0,
-2.369397054522428990E0,
1.896265312988645760E0,
-5.117697348214109710E-1]

#------------------------------------------------
# Generate signals before and after
#------------------------------------------------
squareWave = signal.square(2 * pi * ffs[0] * squareInterval)
filtered_squarewave1 = lfilter(numeratorLPF64HZ, denominatorLPF64HZ, squareWave)
filtered_squarewave = lfilter(taps, 1.0, filtered_squarewave1)
plotSignal(squareWave, filtered_squarewave, squareInterval, 'Square wave', ffs[0])

for ff in ffs:
    sineWave = sin(2*pi*ff*sineInterval)
    filtered_sinewave1 = lfilter(numeratorLPF64HZ, denominatorLPF64HZ, sineWave)
    filtered_sinewave = lfilter(taps, 1.0, filtered_sinewave1)
    plotSignal(sineWave, filtered_sinewave, sineInterval, 'Sine wave', ff)
