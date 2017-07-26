# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 08:46:30 2017

@author: JFan
"""
from pylab import plot, show

def generateTaps(filename):
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
    inputfilename = repository + 'input' + str(ff) +'hzHPF_1.txt'
    outputfilename = repository + 'output' + str(ff) +'hzHPF_1.txt'
    inputs = generateTaps(inputfilename)
    outputs = generateTaps(outputfilename)
    plot(inputs)
    plot(outputs)
    show()

# square signal
inputfilename = repository + 'squareinput10hzHPF_1.txt'
outputfilename = repository + 'squareoutput10hzHPF_1.txt'
inputs = generateTaps(inputfilename)
outputs = generateTaps(outputfilename)
plot(inputs)
plot(outputs)
show()
