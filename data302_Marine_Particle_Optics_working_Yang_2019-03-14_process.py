#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:22:59 2019

@author: mbiddle
"""

import pandas as pd
import os

path = '/Volumes/data302/Marine_Particle_Optics/working/Yang_2019-03-14'

isca_files = []
P_files = []

# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if 'isca.dat' in file:
            isca_files.append(os.path.join(r, file))
        elif 'P' in file:
            P_files.append(os.path.join(r, file))

norm_angle=list(range(2,109))
rows=['scattering_angle']+norm_angle
cols = list(range(0,498))
cols = cols
p_df = pd.DataFrame(columns=cols+['filename','descrip'])
for p in P_files:
    df=pd.read_fwf(p,header=None,columns=cols)
    df['filename']=p.split("/")[-2]+"/"+p.split("/")[-1]
    df['descrip']=rows
    p_df=pd.concat([p_df,df])
    
header = list(p_df.loc[p_df['descrip']=='scattering_angle',list(range(0,498))+['descrip']].iloc[0].values)
for i in range(0,len(header)-1):
    header[i]="sa_"+str(header[i]).replace(".","pt")
header.insert(-1,'filename')
p_df.drop(p_df[p_df['descrip']=='scattering_angle'].index,inplace=True) # remove rows that have scattering_angle
p_df.rename(columns={i:j for i,j in zip(list(p_df.columns.values),header)},inplace=True) # change the column heading
p_df.drop(columns = ['scattering_angle'],inplace=True ) # drop scattering angle column
p_df.reset_index(inplace=True)
p_df.rename(columns = {'index' : 'size_class'},inplace=True)
p_df.sort_values(['filename','size_class'],inplace=True)
p_df.to_csv('/Volumes/data302/Marine_Particle_Optics/766464/1/data/P_combined.csv',header=True,index=False)


sys.exit()
columns=['wavelength','eq_vol_sphere_rad','part_vol','part_proj_area','ext_efficiency','single_scatt_albedo','asymetry_factor']  
isca_df = pd.DataFrame(columns=columns)
for f in isca_files:
    df=pd.read_fwf(f,header=None,names=columns,colspec=[17,17,17,17,17,17,17])
    df['filename']=f.split("/")[-2]+"/"+f.split("/")[-1]
    isca_df=pd.concat([isca_df,df])
    fname=r.split("/")[-1]+f
    print(f)
    print(df.head())
isca_df.sort_values(['filename','eq_vol_sphere_rad'],inplace=True)    

isca_df.to_csv('/Volumes/data302/Marine_Particle_Optics/766421/1/data/isca_combined.csv',header=True,index=False,columns=['wavelength','eq_vol_sphere_rad','part_vol','part_proj_area','ext_efficiency','single_scatt_albedo','asymetry_factor','filename'])


