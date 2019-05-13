#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 13:34:25 2019

@author: mbiddle
"""

import pandas as pd

file = 'Data Maxence Guillemric.xlsx'

dxl = pd.read_excel(file,na_values='nd',header=0,skiprows=[1])

dxl.rename(columns={'Species':'species',
 'pCO2sw':'pco2sw',
 'T ':'T',
 'pHsw':'pHsw',
 'Tank':'Tank',
 'δ11B1':'delta_11B1',
 '2sd':'delta_11B1_2sd',
 'δ11B2':'delta_11B2',
 '2sd.1':'delta_11B2_2sd',
 'δ11Baverage':'delta_11B_avg',
 '2sd.2':'delta_11B_avg_2sd',
 'Li/Ca':'Li_Ca',
 '2sd.3':'Li_Ca_2sd',
 'B/Ca':'B_Ca',
 '2sd.4':'B_Ca_2sd',
 'Mg/Ca':'Mg_Ca',
 '2sd.5':'Mg_Ca_2sd',
 'Sr/Ca':'Sr_Ca',
 '2sd.6':'Sr_Ca_2sd',
 'pHcf ':'pHcf',
 '[CO32-]cf ':'CO3_2_cf',
 '2sd.7':'CO3_2_cf_2sd',
 'DICcf':'DIC_cf',
 '2sd.8':'DIC_cf_2sd'},inplace=True)

dxl['species']=dxl['species'].astype(str).str.replace(" ","_")
filename='/Volumes/data302/CoralCalcifyFluid_pH/767327/1/data/data.csv'
dxl.to_csv(filename,index=False,header=True,float_format="%.2f")