#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 11:21:13 2019

@author: mbiddle
"""

import pandas as pd

filename = 'Datasharing_data_2018.xlsx'
df = pd.read_excel(filename,dtype=str)
df_final=pd.DataFrame()
for col in list(df.columns):
    if col == "any other relevant information that will enable others to understatnd and reuse the data (e.g. published papers)":
        continue
    col2=col.replace(" ","_")
    df_final[col2]=df[col].astype(str).str.replace(",",";")
    
df_final.rename(columns={'locations_where_species_were_collected_(including_lat_and_long_and_cruise_ID_numbers_if_known/applicable':'locations',
                        'sequencing_and_analysis_methods_(including_instrument_names_and_models':'method'},inplace=True)
file='/Volumes/data302/HawaiianFishOrigins/722096/1/data/datasharing_2018.csv'
df_final.to_csv(file,index=False,header=True)