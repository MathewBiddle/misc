#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:34:00 2019

@author: mbiddle
"""

import pandas as pd

trans = 'BCO-DMO_transcriptomes.xlsx'
dft = pd.read_excel(trans,parse_dates=False,dtype=str)

dft['Experiment Date']=dft['Experiment Date'].astype(str).str.replace(" 00:00:00","")
dft.rename(columns={'Lat.1':'lat',
                    'Lon.1':'lon',
                    'Lat':'Lat_dm',
                    'Lon':'Lon_dm',
                    'Sample ID':'sample_id', 
                    'SRA Accession':'SRA_Accession',
                    'SRA Study':'SRA_Study', 
                    'Dive ID':'Dive_ID', 
                    'Collection ID':'Collection_ID', 
                    'Vent Field':'Vent_field',
                    'Depth (m)':'Depth',
                    'Experiment Date':'Experiment_date',
                    'Experiment Number':'Experiment_number', 
                    'Aquaria Number':'Aquaria_Number', 
                    'Individual ID':'Individual_ID',
                    'weight (g)':'weight'},inplace=True)
dft['Vent_field']=dft['Vent_field'].astype(str).str.replace("Tu'I Malila","TuI Malila")
dft['Lat_dm']=dft['Lat_dm'].astype(str).str.replace("°","")
dft['Lat_dm']=dft['Lat_dm'].astype(str).str.replace("′","")
dft['Lon_dm']=dft['Lon_dm'].astype(str).str.replace("°","")
dft['Lon_dm']=dft['Lon_dm'].astype(str).str.replace("′","")

filename = '/Volumes/data302/Eco_Dyn_W_Pacific_Vents/767265/1/data/transcriptomes.csv'
dft.to_csv(filename,index=False,header=True)
sys.exit()



s16 = 'BCO-DMO_16S.xlsx'

ds16 = pd.read_excel(s16,parse_dates=False,
                    dtype=str)
ds16['Date']=ds16['Date'].astype(str).str.replace(" 00:00:00","")
ds16['ISO_datetime'] = pd.to_datetime(ds16['Date']+ ' ' +ds16['Time'])

la = "-"+ds16['Lat'].astype(str).str.split(" ",n=1,expand=True)
ds16['lat']=la[0]
lo = "-"+ds16['Lon'].astype(str).str.split(" ",n=0,expand=True)
ds16['lon']=lo[0]

ds16.rename(columns={'Collection ID':'Collection_ID',
                     'Depth (m)':'Depth',
                     'SRA Accession':'SRA_Accession',
                     'SRA Study':'SRA_Study',
                     'Sample ID':'Sample_ID',
                     'Vent field':'Vent_field'},inplace=True)

ds16['Vent_field']=ds16['Vent_field'].astype(str).str.replace("Tu'i Malila","Tui Malila")

filename = '/Volumes/data302/Eco_Dyn_W_Pacific_Vents/767230/1/data/16s.csv'
ds16.to_csv(filename,index=False,header=True,date_format='%Y-%m-%dT%H:%M:%S')

