import pandas as pd

dfile = 'Hansel BCO-DMO Data.xlsx'

df = pd.read_excel(dfile,header=[0],sheet_name=['CTD Data','Full Data for discrete depths'],skiprows=[1],dtype=str)

df['Full Data for discrete depths']['ISO_datetime_UTC']=pd.to_datetime(
	df['Full Data for discrete depths']['Year']+' '+\
	df['Full Data for discrete depths']['Month']+' '+\
	df['Full Data for discrete depths']['Day']+' '+\
	df['Full Data for discrete depths']['Time'],utc=True)

df['CTD Data']['ISO_datetime_UTC']=pd.to_datetime(
	df['CTD Data']['Year']+' '+\
	df['CTD Data']['Month']+' '+\
	df['CTD Data']['Day']+' '+\
	df['CTD Data']['Time'],utc=True)

df['Full Data for discrete depths']['sheet']='Full_Data_for_discrete_depths'
df['Full Data for discrete depths'].rename(columns={'Florescence ':'Florescence','Salinity ':'Salinity','Chlorophyll ':'Chlorophyll','Lat':'lat','Long':'long'},inplace=True)
## define precision on write using df.to_string https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_string.html
print(df['Full Data for discrete depths'].head())
df['Full Data for discrete depths'].to_csv('Full_Data_for_discrete_depths.csv',date_format='%Y-%m-%dT%H:%M:%S%z',index=False)

df['CTD Data']['sheet']='CTD_Data'
print(df['CTD Data'].head())
df['CTD Data'].to_csv('CTD_Data.csv',date_format='%Y-%m-%dT%H:%M:%S%z',index=False)

df_final=pd.concat([df['Full Data for discrete depths'],df['CTD Data']],ignore_index=True,sort=False)

# map column names
df_final.rename(columns={
        'Beam Transmission':'Beam_Transmission',
        'NO2-':'NO2',
        'NO3-':'NO3',
        'Std Dev':'Chloro_sd',
        'Avg Nanoeuks ':'Nanoeuks',
        'Std dev':'Nanoeuks_sd',
        'Avg Picoeuks ':'Picoeuks',
        'Std dev.1':'Picoeuks_sd',
        'Avg Synechococcus':'Synechococcus',
        'Std dev.2':'Synechococcus_sd',
        'Avg Bacteria ':'Bacteria',
        'Std dev.3':'Bacteria_sd',
        'Std dev.4':'DOC_sd',
        'Total O2-':'Tot_O2',
        'std dev':'Tot_O2_sd',
        'Particle O2-':'Part_O2',
        'std dev.1':'Part_O2_sd',
        'Net H2O2':'Net_H2O2',
        'Std dev.5':'Net_H2O2_sd',
        'Gross H2O2':'Gross_H2O2',
        'Std Dev.1':'Gross_H2O2_sd',
        'Total dHg':'Total_dHg',
        'Std Dev.2':'Total_dHg_sd',
        'Hg(0)':'Hg_0',
        'Std Dev.3':'Hg_0_sd',
        'dMn(II)':'dMn_II',
        'Std Dev.4':'dMn_II_sd',
        'dMn(T) ':'dMn_T',
        'Std Dev.5':'dMn_T_sd',
        'dMn(III)-L':'dMn_III_L',
        'Std Dev.6':'dMn_III_L_sd'
        },inplace=True)

## to convert formats of specific columns
#df_final.replace('nd',np.NaN,inplace=True)
#print(df_final['Chlorophyll'].tail())
#df_final[["lat","long","Chlorophyll"]]=df_final[["lat","long","Chlorophyll"]].apply(pd.to_numeric)
#df_final["lat"]=df_final["lat"].map(lambda x: '%2.5f' % x)
#df_final["long"]=df_final["long"].map(lambda x: '%2.5f' % x)
#df_final["Chlorophyll"]=df_final["Chlorophyll"].map(lambda x: '%1.2f' % x)
#print(df_final['Chlorophyll'].tail())

## reorganize the data columns
cols=df_final.columns.tolist()
cols.insert(7, cols.pop(-2))
df_final=df_final[cols]

#save the data
df_final.to_csv('../../765327/1/data/combined.csv',date_format='%Y-%m-%dT%H:%M:%SZ',index=False)