# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 08:46:30 2017
Plot original signal and filtered signal generated by ASF dsp library
@author: JFan
"""
from pylab import plot, show, title

def generateFile(filename):
    ints = []
    with open(filename) as f:
       data = [line.strip().split() for line in f.readlines()]
    for record in data:
        ints.append(int(record[1]))
    f.close()
    return ints

filtertype = input('Enter the type of filter(for example HPF_1, LPF_1):')
repository = 'C:\\Users\\jfan\\workspace\\digitalFilter\\dsplib\\' + filtertype + '\\'

ffs = [1, 10, 100, 1000]
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
