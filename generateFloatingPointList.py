# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 13:41:21 2017
Generate fixed point coefficients from float point coefficients.
@author: JFan
"""
from os import listdir

directory = 'C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients\\'
output_directory = 'C:\\Users\\jfan\\workspace\\digitalFilter\\coefficients_list\\'
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

            with open(output_directory + names[0] + '_list.txt', 'w') as g:
                for idx in range(len(floats)):
                    g.write(str(floats[idx]))
                    if idx+1 != len(floats):
                        g.write(',\n')
            g.close()
    f.close()
