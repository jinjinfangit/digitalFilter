# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:57:10 2017

@author: JFan
"""

class Utils:
    def __init__(self, gain, sample_rate, qfactor):
        self.gain = gain
        self.sample_rate = sample_rate
        self.qfactor = qfactor

    def generateTaps(self, filename):
        floats = []
        with open(filename) as f:
            for line in f:
                floats.extend([float(number)* self.gain for number in line.split()])
        f.close()
        return floats, len(floats)

    def generateDownsample(self, inputs):
        outputs = list()
        idx = 0
        while idx < self.sample_rate/self.qfactor:
            outputs.append(inputs[idx*self.qfactor])
            idx = idx + 1
        return outputs

    def generateUpsample(self, inputs, sample_rate, lfactor):
        outputs = list()
        for idx_input in range(sample_rate):
            for idx in range(lfactor):
                outputs.append(inputs[idx_input])
        return outputs
