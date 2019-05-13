#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:58:17 2019

@author: mbiddle
"""

import pandas as pd

dfile = 'Table_1_OA_SAMPLES (1).xlsx'

df = pd.read_excel(dfile,header=[0],sheet_name=['SRA_data','Attributes'],dtype=str)

df['Attributes']['ISO_datetime_UTC']=pd.to_datetime(df['Attributes']['collection_date'],utc=True)
df['Attributes'].rename(columns ={'accession':'biosample_accession'},inplace=True)
df_final=pd.merge(df['Attributes'],df['SRA_data'],how='outer',on=['biosample_accession','bioproject_accession'])

lat_lon=df_final['lat_lon'].str.split(' ',n=0,expand=True)
if lat_lon[3].unique()[0] == 'W':
    lon_adj = '-'
else:
    lon_adj = ''  
if lat_lon[1].unique()[0] == 'S':
    lat_adj = '-'
else:
    lat_adj = ''
df_final['lat']=lat_adj+lat_lon[0]
df_final['lon']=lon_adj+lat_lon[2]
df_final.replace('nan','nd',inplace=True)
cols=df_final.columns.tolist()
cols.insert(-2,cols.pop(14))
df_final=df_final[cols]
df_final.to_csv('../../765668/1/data/OA_samples.csv',index=False,date_format='%Y-%m-%dT%H:%M:%SZ')