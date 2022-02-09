#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 14:13:37 2019

@author: mbiddle
"""

import pandas as pd

filename = 'PROJECT 757587 DATA.xlsx'

dxl = pd.read_excel(filename,
                    sheet_name=['1538677 data','Metadata','qPCR parameters','Literature Cited'],
                    nrows=37,
                    dtype=str)

#process = 'data'
process = 'qpcr'

if process == 'data':
    df_data=dxl['1538677 data']
    ## convert lat/lons
    latitudes=[]
    longitudes=[]
    long=list(df_data['Longitude (degrees and deciminutes W)'].values)
    for lon in long:
        lon.replace("\'","'")
        lons=lon.split(' ')
        if len(lons)!=4:
            lons.insert(-1,"0\"")
        lond = float(lons[0].replace("°",""))
        lonmin = float(lons[1].replace("'",""))
        lonsec = float(lons[2].replace("\"",""))
        lonh = lons[3]
        print(lond,lonmin,lonsec,lonh)
        longitude = lond+(lonmin+(lonsec/60))/60
        if lonh == 'W':
            longitude=longitude*-1
        longitude="%6.4f"%longitude
        longitudes.append(longitude)
        #print(longitude)
    df_data['lon']=longitudes
    
    lati=list(df_data['Latitude (degrees and deciminutes N)'].values)
    for lat in lati:
        lat.replace("\'","'")
        lats=lat.split(' ')
        if len(lats)!=4:
            lats.insert(-1,"0\"")
        latd = float(lats[0].replace("°",""))
        latmin = float(lats[1].replace("'",""))
        latsec = float(lats[2].replace("\"",""))
        lath = lats[3]
        #print(latd,latmin,latsec,lath)
        latitude = latd+(latmin+(latsec/60))/60
        if lath == 'S':
            latitude=latitude*-1
        latitude="%6.4f"%latitude
        latitudes.append(latitude)
        #print(latitude)
    df_data['lat']=latitudes
    
    # do some data clean up
    for col in list(df_data.columns):
        df_data[col]=df_data[col].str.replace(" × 10","e") # adjust x10^ to e
        if any(df_data[col].str.contains("±")): # pull out standard deviation into it's own col
            new=df_data[col].str.split("±",expand=True)
            df_data[col]=new[0]
            df_data[col+"_sd"]=new[1]
        elif any(df_data[col].str.contains("°")):
            df_data[col]=df_data[col].str.replace("°","")
            df_data[col]=df_data[col].str.replace("\"","")
            df_data[col]=df_data[col].str.replace("'","")
    
    
    df_data.rename(columns = {'Cruise Identifier':"Cruise_ID",
     'Station':"Sta",
     'Region':"Region",
     'Sample depth (m)':"depth",
     'Latitude (degrees and deciminutes N)':"Latitude",
     'Longitude (degrees and deciminutes W)':"Longitude",
     'Date':"Date",
     'Bacterial 16S rRNA (109 copies L-1)':"Bacterial_16S_rRNA",
     'Thaumarchaeal 16S rRNA  (109 copies L-1)':"Thaumarchaeal_16S_rRNA",
     'WCA amoA  (109 copies L-1)':"WCA_amoA",
     'WCB amoA  (109 copies L-1)':"WCB_amoA",
     'Nitrospina 16S rRNA  (109 copies L-1)':"Nitrospina_16S_rRNA",
     '15N added (nM final concentration)':"N15_added",
     'Ammonia oxidation (nmol L-1 d-1)':"Ammonia_Oxidation",
     '15N oxidation from PUT (nmol L-1 d-1)':"N15_ox_from_PUT",
     '15N oxidation from GLU (nmol L-1 d-1)':"N15_ox_from_GLU",
     '15N oxidation from UREA (nmol L-1 d-1)':"N15_ox_from_UREA",
     '15N oxidation from DAE (nmol L-1 d-1)':"N15_ox_from_DAE",
     '15N oxidaton from DAP (nmol L-1 d-1)':"N15_ox_from_DAP",
     '15N oxidation from ARG (nmol L-1 d-1)':"N15_ox_from_ARG",
     'Nitrate (mM)':"Nitrate",
     'Nitrite (mM)':"Nitrite",
     'Ammonium (mM)':"Ammonium",
     'Urea (mM)':"Urea",
     'Silicate (mM)':"Silicate",
     'Phosphate (mM)':"Phosphate",
     'Temperature (oC)':"Temperature",
     'Salinity (PSU)':"Salinity",
     'Dissolved oxygen mL L-1':"Diss_Oxygen",
     'Relative Fluorescence':"Relative_Fluor",
     'Attenuation Coefficient, Kz (m-1)':"Atten_Coeff",
     'Comment label':"comment",
     'Ammonia oxidation (nmol L-1 d-1)_sd':"Ammonia_Oxidation_sd",
     '15N oxidation from PUT (nmol L-1 d-1)_sd':"N15_ox_from_PUT_sd",
     '15N oxidation from GLU (nmol L-1 d-1)_sd':"N15_ox_from_GLU_sd",
     '15N oxidation from UREA (nmol L-1 d-1)_sd':"N15_ox_from_UREA_sd",
     '15N oxidation from DAE (nmol L-1 d-1)_sd':"N15_ox_from_DAE_sd",
     '15N oxidaton from DAP (nmol L-1 d-1)_sd':"N15_ox_from_DAP_sd",
     '15N oxidation from ARG (nmol L-1 d-1)_sd':"N15_ox_from_ARG_sd",
     'lon':"lon",
     'lat':"lat"},inplace=True)
    
    columns=['Cruise_ID',
     'Sta',
     'Region',
     'depth',
     'lon',
     'lat',
     'Latitude',
     'Longitude',
     'Date',
     'ISO_Date',
     'Bacterial_16S_rRNA',
     'Thaumarchaeal_16S_rRNA',
     'WCA_amoA',
     'WCB_amoA',
     'Nitrospina_16S_rRNA',
     'N15_added',
     'Ammonia_Oxidation',
     'Ammonia_Oxidation_sd',
     'N15_ox_from_PUT',
     'N15_ox_from_PUT_sd',
     'N15_ox_from_GLU',
     'N15_ox_from_GLU_sd',
     'N15_ox_from_UREA',
     'N15_ox_from_UREA_sd',
     'N15_ox_from_DAE',
     'N15_ox_from_DAE_sd',
     'N15_ox_from_DAP',
     'N15_ox_from_DAP_sd',
     'N15_ox_from_ARG',
     'N15_ox_from_ARG_sd',
     'Nitrate',
     'Nitrite',
     'Ammonium',
     'Urea',
     'Silicate',
     'Phosphate',
     'Temperature',
     'Salinity',
     'Diss_Oxygen',
     'Relative_Fluor',
     'Atten_Coeff',
     'comment'
     ]
    df_data[df_data=="nan"]=None
    
    float_params=['Nitrate',
                  'Nitrite',
                  'Ammonium',
                  'Urea',
                  'Diss_Oxygen',
                  'lat',
                  'lon']
    for param in float_params:
        if any(df_data[param].str.contains("BDL")):
            df_data[param]=df_data[param].str.replace("BDL","-9999")
        df_data[param]=df_data[param].astype(float)
        if any(df_data[param]==-9999):
            df_data[param]=df_data[param].round(decimals=2)
            df_data[param]=df_data[param].replace(-9999.00,"BDL")
    df_data['ISO_Date']=pd.to_datetime(df_data['Date'],infer_datetime_format=True)
    df_data['Sta']=df_data['Sta'].str.replace(". ","_").replace(" ","_").replace("-","_")
    filename='/Volumes/data302/DON_Oxidation/767048/1/data/DON_Oxidation.csv'
    df_data.to_csv(filename,header=True,index=False,columns=columns,float_format="%4.2f")
    
elif process == 'qpcr':
    df_qpcr=dxl['qPCR parameters']
    
    df_qpcr.drop(df_qpcr.index[-1], axis=0,inplace=True) # drop last row
    df_qpcr.reset_index(inplace=True)
    if any(df_qpcr['index'].str.contains('Probea')):
        df_qpcr['index']=df_qpcr['index'].str.replace("Probea","Probe")
    
    df_qpcr=df_qpcr.T
    df_qpcr.reset_index(inplace=True)
    df_qpcr.fillna("Missing",inplace=True)
    df_qpcr.columns=df_qpcr.iloc[0]
    df_qpcr.drop(df_qpcr.index[0], axis=0,inplace=True)
    
    variables=sorted(set(list(df_qpcr.columns)))
    variables.remove("Missing")
    
    df_final=pd.DataFrame(columns = ['Probe'])#columns = variables)
    df_final['Forward_primer']=df_qpcr['Forward primer'].astype(str).str.cat(df_qpcr.iloc[:,[2]].astype(str), sep="; ")
    df_final['Reverse_primer']=df_qpcr['Reverse primer'].astype(str).str.cat(df_qpcr.iloc[:,[4]].astype(str), sep="; ")
    df_final['Probe']=df_qpcr['Probe'].astype(str).str.cat(df_qpcr.iloc[:,[6]].astype(str), sep="; ")
    df_final['Probe']=df_final['Probe'].str.replace("nan; nan","")
    df_final['Cycling_conditions']=df_qpcr['Cycling conditions'].astype(str).str.cat(df_qpcr.iloc[:,[9]].astype(str), sep=" ")
    df_final['Cycling_conditions']=df_final['Cycling_conditions'].astype(str).str.cat(df_qpcr.iloc[:,[10]].astype(str), sep=" ")
    df_final['Cycling_conditions']=df_final['Cycling_conditions'].astype(str).str.cat(df_qpcr.iloc[:,[11]].astype(str), sep="; ")
    df_final['Cycling_conditions']=df_final['Cycling_conditions'].astype(str).str.cat(df_qpcr.iloc[:,[12]].astype(str), sep="; ")
    df_final['Cycling_conditions']=df_final['Cycling_conditions'].astype(str).str.cat(df_qpcr.iloc[:,[13]].astype(str), sep="; ")
    df_final['Cycling_conditions']=df_final['Cycling_conditions'].str.replace(" nan;","")
    df_final['Efficiency']=df_qpcr['Efficiency (%)']
    df_final['Limit_of_Detection_template']=df_qpcr['Limit of Detection template']
    df_final['Limit_of_Detection_sample']=df_qpcr['Limit of Detection sample']
    df_final['Number_plates_run']=df_qpcr['Number plates run']
    df_final['Reference']=df_qpcr['Reference(s)']
    df_final['qPCR_Parameters']=df_qpcr['index']

    for col in list(df_final.columns):
        df_final[col]=df_final[col].str.replace(","," ")
        df_final[col]=df_final[col].str.replace("º"," ")
        df_final[col]=df_final[col].str.replace(" copies uL-1 of template","")
        df_final[col]=df_final[col].str.replace(" copies L-1 of sample","")

    outcol=['qPCR_Parameters','Probe', 'Forward_primer', 'Reverse_primer', 'Cycling_conditions',
       'Efficiency', 'Limit_of_Detection_template',
       'Limit_of_Detection_sample', 'Number_plates_run', 'Reference']
    
    filename='/Volumes/data302/DON_Oxidation/767141/1/data/qPCR.csv'
    df_final.to_csv(filename,header=True,index=False,columns=outcol)
