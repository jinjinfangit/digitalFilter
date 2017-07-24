# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:46:26 2017

@author: JFan
"""

from scipy.signal import lfilter

class IIRFilter:
    #3 Pole Adj Gauss LPF
    numeratorLPF1HZ = (5.678524821710300150E-9,
    1.703557446513090490E-8,
    1.703557446513090490E-8,
    5.678524821710300150E-9
    )
    denominatorLPF1HZ = (1.000000000000000000E0,
    -2.992165429719710450E0,
    2.984359105193572060E0,
    -9.921936300456629000E-1)

    def filter(self, origin):
        return lfilter(self.numeratorLPF1HZ,
                           self.denominatorLPF1HZ,
                           origin)
