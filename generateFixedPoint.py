# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:41:21 2017
Generate fixed point coefficients from float point coefficients.
@author: JFan
"""

import math

from os import listdir
from os.path import isfile, join

BITS = 16
directory = "C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients\\"
output_directory = "C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients_fixed\\"
files = [f for f in listdir(directory)]

for file in files:
    if file != 'LPF_1.txt':
        with open(directory + file) as f:
            names = file.split('.')
            # Generate coefficient list
            floats = list()
            for line in f:
                floats.extend([float(number) for number in line.split()])

            # Get maxinum abs value
            max_floats = max([math.fabs(number) for number in floats])
            expo = math.floor(math.log2((math.pow(2, BITS-1)-1)/max_floats))
            # Generate normalized list
            # Generate final lists
            with open(output_directory + names[0] + '_fixedpoint.txt', 'w') as g:
                for idx in range(len(floats)):
                    g.write(str(math.ceil(math.pow(2,expo)*floats[idx])))
                    if idx+1 != len(floats):
                        g.write(', ')
            g.close()
        f.close()
