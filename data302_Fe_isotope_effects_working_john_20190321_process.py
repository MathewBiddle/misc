#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 09:26:00 2019

@author: mbiddle
"""

import pandas as pd

filename = 'BCO DMO data.xlsx'

dxl = pd.read_excel(filename,
                    dtype=str)

dxl.rename(columns={'[Reductant]':'Reductant_conc',
                    'Sample ID':'Sample_ID'},inplace=True)
filename='/Volumes/data302/Fe_isotope_effects/767208/1/data/BCO_DMO_Data.csv'
dxl.to_csv(filename,header=True,index=False)