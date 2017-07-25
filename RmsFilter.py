# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:46:26 2017

@author: JFan
"""

import numpy as np

class RmsFilter:
    def __init__(self, sample_rate, window_size):
        """
        Return a notch filter depending on the frequency
        """
        self.sample_rate = sample_rate
        self.window_size = window_size

    def filter(self, origin):
        output = list()
        start = 0
        while start < self.sample_rate:
            sublist = origin[start:start+self.window_size]
            output.append(np.sqrt(np.mean(sublist**2)))
            start += self.window_size
        return output
