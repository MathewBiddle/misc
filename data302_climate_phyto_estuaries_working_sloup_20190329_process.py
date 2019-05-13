#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:17:07 2019

@author: mbiddle
"""
import pandas as pd

file = 'NR database BCO-DMO oce-0825466.xlsx'

dxl = pd.read_excel(file,sheet_name=None,na_values='nd')#,parse_dates=[['Date','YSI_Time (H:mm:ss)']])

df_data = dxl['Data']
df_data['Date']=df_data['Date'].astype(str).str.replace(" 00:00:00","")
df_data['ISO_DateTime']=pd.to_datetime(df_data['Date'].astype(str)+" "+df_data['YSI_Time (H:mm:ss)'].astype(str))

df_data_final=pd.merge(df_data,dxl['Station list'],how='left',on='Station')
filename='WQ_data.csv'
df_data_final.to_csv(filename,index=False,header=True)
# this looks good, thinking about combining with YSI data

df_ysi = dxl['YSI Profile Data']
df_ysi.drop(columns=['TimeOriginal', 'TimeConverted', 'CalcDOSat', 'CalDOconc', 'Ts', 'SatDO_mL/L', 'SatDO_µM', 'SatDO_mg/L', 'Coeff. from Garcia & Gordon 1992 L&O','Unnamed: 23'],inplace=True)
df_ysi['Date']=df_ysi['Date'].astype(str).str.replace(" 00:00:00","")
df_ysi['ISO_DateTime']=pd.to_datetime(df_ysi['Date'].astype(str)+" "+df_ysi['Time'].astype(str))

df_ysi_final=pd.merge(df_ysi,dxl['Station list'],how='left',on='Station')

# TO-DO check on last few columns and see if we need to remove