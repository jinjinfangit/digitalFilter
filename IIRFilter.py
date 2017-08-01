# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:46:26 2017

@author: JFan
"""

from scipy.signal import lfilter

class IIRFilter:
    #3 Pole Adj Gauss LPF
    numeratorLPF1HZ = [5.678524821710300150E-9,
    1.703557446513090490E-8,
    1.703557446513090490E-8,
    5.678524821710300150E-9
    ]
    denominatorLPF1HZ = [1.000000000000000000E0,
    -2.992165429719710450E0,
    2.984359105193572060E0,
    -9.921936300456629000E-1]

    numeratorLPF64HZ = [1.887315455600753420E-3,
    5.661946366802261820E-3,
    5.661946366802261820E-3,
    1.887315455600753420E-3]

    denominatorLPF64HZ = [1.000000000000000000E0,
    -2.369397054522428990E0,
    1.896265312988645760E0,
    -5.117697348214109710E-1]

    numeratorLPF100HZ = [4.939247730931259460E-3,
                         6.172438968326678930E-3,
                         6.172438968326678040E-3,
                         4.939247730931259460E-3
    ]
    denominatorLPF100HZ = [1.000000000000000000E0,
                           -2.385610153211325190E0,
                           1.946248322291393330E0,
                           -5.384147956815525050E-1]

    def __init__(self):
        self.IIRFilterConf = dict()
        self.IIRFilterConf = {
                'LPF_1HZ' : {
                        'numerator' : self.numeratorLPF1HZ,
                        'denominator' : self.denominatorLPF1HZ},
                'LPF_64HZ' : {
                        'numerator' : self.numeratorLPF64HZ,
                        'denominator' : self.denominatorLPF64HZ},
                'LPF_100HZ' : {
                        'numerator' : self.numeratorLPF100HZ,
                        'denominator' : self.denominatorLPF100HZ},
        }

    def filter(self, type, origin):
        if (self.IIRFilterConf[type]):
            return lfilter(self.IIRFilterConf[type]["numerator"],
                           self.IIRFilterConf[type]["denominator"],
                           origin)
