# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:46:17 2017

@author: JFan
"""

class FilterConstant:
    sample_rate = 2048
    window_size = 32
    qfactor = 8
    sensorConfiguration = {
        'External' : {
                       'Gain': 1,
                       'T1': '50HZ/60HZ',
                       'T2': None,
                       'T3': {'Type': 'LPF', 'highcut': 64},
                       'T4': 8,
                       'T5': None,
                       'T6': None,
                       'T7': None
                     },
        'EEG-SCP/DC' : {
                       'Gain': 25,
                       'T1': '50HZ/60HZ',
                       'T2': {'Type': 'LPF', 'highcut': 64},
                       'T3': {'Type': 'LPF', 'highcut': 64},
                       'T4': 8,
                       'T5': None,
                       'T6': None,
                       'T7': None
                       },
        'EEG-EP' :  {
                       'Gain': 25,
                       'T1': '50HZ/60HZ',
                       'T2': {'Type': 'HPF', 'lowcut': 1},
                       'T3': {'Type': 'BPF', 'lowcut': 1, 'highcut':64},
                       'T4': 8,
                       'T5': None,
                       'T6': None,
                       'T7': None
                    },
        'EEG' :     {
                       'Gain': 25,
                       'T1': '50HZ/60HZ',
                       'T2': None,
                       'T3': {'Type': 'LPF', 'lowcut': 0, 'highcut':64},
                       'T4': 8,
                       'T5': None,
                       'T6': None,
                       'T7': None
                    },
        'EKG' :     {
                       'Gain': 25,
                       'T1': '50HZ/60HZ',
                       'T2': {'Type': 'BPF', 'lowcut': 1, 'highcut':64},
                       'T3': {'Type': 'BPF', 'lowcut': 1, 'highcut':64},
                       'T4': 8,
                       'T5': None,
                       'T6': None,
                       'T7': None
                    },
    }
