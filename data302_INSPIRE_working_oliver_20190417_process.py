import numpy as np
import pandas as pd

files = ['chl.csv','dfe.csv','no3.csv','pon.csv']

df_final=pd.DataFrame(columns=['Station','LocalDate','Depth'])#,'Chla','DissFe','TotalDIN','PON'])

for file in files:
   df=pd.read_csv(file,parse_dates=['LocalDate'],infer_datetime_format=True,dtype=str)
   df['Depth']=pd.to_numeric(df['Depth'])
   df_final=pd.merge(df_final,df,how='outer',on=['Station','LocalDate','Depth'])


df_loc = pd.read_csv('station_locations.csv',dtype=str)
df_loc.rename(columns={'station':'Station'},inplace=True)
df_final=pd.merge(df_final,df_loc,how='outer',on=['Station'])
df_final.sort_values(by=['LocalDate','Station','Depth'],inplace=True)
df_final.to_csv('../../765081/1/data/combined.csv',index=False)
