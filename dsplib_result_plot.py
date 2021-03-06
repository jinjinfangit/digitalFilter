# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 08:46:30 2017
Plot original signal and filtered signal generated by ASF dsp library
@author: JFan
"""
from pylab import plot, show, title
from PlotSignal import PlotSignal
from FilterConstant import FilterConstant

def generateFile(filename):
    ints = []
    with open(filename) as f:
       data = [line.strip().split() for line in f.readlines()]
    for record in data:
        ints.append(int(record[1]))
    f.close()
    return ints

filtertype = input('Enter the type of filter:')
repository = 'C:\\Users\\jfan\\workspace\\digitalFilter\\dsplib\\' + filtertype + '\\'
if filtertype == 'RMS':
    inputfilename = repository + 'input.txt'
    inputs = generateFile(inputfilename)
    outputfilename = repository + 'output.txt'
    outputs = generateFile(outputfilename)
    plotsignal = PlotSignal(1, FilterConstant.sample_rate,
                            FilterConstant.qfactor, 0, 60)
    plotsignal.plotRMSWindow(inputs, outputs[:64], FilterConstant.window_size)
    show()
    inputfilename = repository + 'inputSqr.txt'
    inputs = generateFile(inputfilename)
    outputfilename = repository + 'outputSqr.txt'
    outputs = generateFile(outputfilename)
    plotsignal.plotRMSWindow(inputs, outputs[:64], FilterConstant.window_size)
    show()
elif filtertype == 'downsample':
    inputfilename = repository + 'input.txt'
    inputs = generateFile(inputfilename)
    outputfilename = repository + 'output.txt'
    outputs = generateFile(outputfilename)
    plotsignal = PlotSignal(1, FilterConstant.sample_rate,
                            FilterConstant.qfactor, 0, 60)
    plotsignal.plotDownSampling(inputs, outputs[:256])
    show()
    inputfilename = repository + 'inputSqr.txt'
    inputs = generateFile(inputfilename)
    outputfilename = repository + 'outputSqr.txt'
    outputs = generateFile(outputfilename)
    plotsignal.plotDownSampling(inputs, outputs[:256])
    show()
elif filtertype == 'upsample':
    lfactors = [4, 32]
    for lfactor in lfactors:
        inputfilename = repository + 'input.txt'
        inputs = generateFile(inputfilename)
        outputfilename = repository + 'output' + str(lfactor) + '.txt'
        outputs = generateFile(outputfilename)
        plotsignal = PlotSignal(1, FilterConstant.sample_rate,
                                FilterConstant.qfactor, 0, 60)
        plotsignal.plotUpSampling(inputs, outputs, 64, lfactor)
        show()
        inputfilename = repository + 'inputSqr.txt'
        inputs = generateFile(inputfilename)
        outputfilename = repository + 'outputSqr' + str(lfactor) + '.txt'
        outputs = generateFile(outputfilename)
        plotsignal.plotUpSampling(inputs, outputs, 64, lfactor)
        show()
else:
    ffs = [1, 10, 50, 60, 100, 1000]
    #sinu signal
    for ff in ffs:
        inputfilename = repository + 'input' + str(ff) +'hz.txt'
        outputfilename = repository + 'output' + str(ff) +'hz.txt'
        inputs = generateFile(inputfilename)
        outputs = generateFile(outputfilename)
        plot(inputs)
        plot(outputs)
        title('Digital Filter(%s) %dHZ' %(filtertype, ff))
        show()

    # square signal

    inputfilename = repository + 'squareinput10hz.txt'
    outputfilename = repository + 'squareoutput10hz.txt'
    inputs = generateFile(inputfilename)
    outputs = generateFile(outputfilename)
    title('Digital Filter(%s) 10HZ' %filtertype)
    plot(inputs)
    plot(outputs)
    show()

