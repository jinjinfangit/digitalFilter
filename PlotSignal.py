# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:12:07 2017

@author: JFan
"""

from pylab import figure, plot, xlabel, ylabel, ylim, title, grid, show, subplot, subplots_adjust
import matplotlib.pyplot as plt
from scipy.signal import freqz
from numpy import pi, absolute, sqrt, arange
from scipy import fft
from matplotlib import gridspec

class PlotSignal:
    def __init__(self, gain, sample_rate, qfactor, lowcut, highcut):
        self.gain = gain
        self.sample_rate = sample_rate
        self.qfactor = qfactor
        self.lowcut = lowcut
        self.highcut = highcut

    def plotFilter(self, taps):
        figure(1)
        subplot(2,1,1)
        plot(taps, 'bo-', linewidth=2)
        title('Filter Coefficients (%d taps)' % len(taps))
        grid(True)
        subplot(2,1,2)
        # First plot the desired ideal response as a green(ish) rectangle.
        rect = plt.Rectangle((self.lowcut, 0), self.highcut - self.lowcut, 1.0 * self.gain,
                             facecolor="#60ff60", alpha=0.2)
        plt.gca().add_patch(rect)
        # Plot the frequency response of each filter
        w, h = freqz(taps, worN=8000)
        plt.plot((w/pi)*(self.sample_rate/2.0), absolute(h), linewidth=2)
        plt.plot([0, 0.5 * self.sample_rate], [self.gain * sqrt(0.5),
                                               self.gain * sqrt(0.5)],'--')
        xlabel('Frequency (Hz)')
        ylabel('Gain')
        title('Frequency Response')
        ylim(-0.05, 1.5 * self.gain)
        grid(True)
        subplots_adjust(hspace=.5)
        plt.show()

    def plotSpectrum(self, ax, signal, color):
        """
        Plot a Single-Sided Amplitude Spectrum of signal(t)
        """
        n = len(signal) # length of the signal
        k = arange(n)
        T = n/self.sample_rate
        frq = k/T # two sides frequency range
        frq = frq[range(int(n/2))] # one side frequency range

        Y = fft(signal)/n # fft computing and normalization
        Y = Y[range(int(n/2))]

        ax.plot(frq, abs(Y), color) # plotting the spectrum
        xlabel('Freq (Hz)')
        ylabel('Gain')

    def plotSignal(self, before, after, interval, title, freq, delay):
        """
        Plot the original and filtered signals both in time domain and in
        frequency domain.
        """
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
        self.plotSpectrum(ax2, before, 'b')
        plt.title('Gain vs Freq(before)')
        ax3 = fig.add_subplot(gs[1,1])
        self.plotSpectrum(ax3, after, 'r')
        plt.title('Gain vs Freq(after)')
        gs.update(wspace=0.5, hspace=0.5)
        plt.suptitle('FIR %s(%dHz)' %(title,freq))
        show()

    def plotDownSampling(self, before, after):
         subplot(2,1,1)
         plt.stem(range(self.sample_rate), before, '-.')
         subplot(2,1,2)
         plt.stem(range(int(self.sample_rate/self.qfactor)), after, '-.')
         plt.show()
