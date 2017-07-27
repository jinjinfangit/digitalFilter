# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:41:21 2017
Generate fixed point coefficients from float point coefficients.
@author: JFan
"""

import math

from os import listdir

directory = 'C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients\\'
output_directory = 'C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients_fixed\\'
files = [f for f in listdir(directory)]

for file in files:
    with open(directory + file) as f:
        if 'LPF_1.txt' == file:
            continue
        names = file.split('.')
        # Generate coefficient list
        floats = list()
        for line in f:
            floats.extend([float(number) for number in line.split()])

        if 'LPF_1' not in file:
            print("11" + file)
            BITS = 16
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
        elif 'ator' in file:
            print("22" + file)
            BITS = 32
            fraction = float(1/math.pow(2, BITS-1))
            with open(output_directory + names[0] + '_fixedpoint.txt', 'w') as g:
                for idx in range(len(floats)):
                    g.write(str(math.ceil(floats[idx]/fraction)))
                    if idx+1 != len(floats):
                        g.write(', ')
            g.close()
    f.close()
