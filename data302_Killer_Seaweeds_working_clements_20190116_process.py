## Python 3.7
import pandas as pd
import numpy as np
lat=-18.2057
lon=177.67

## Frequency
#file1 = 'Clements and Hay 2019_Nature E&E_Coral Species Frequency .xlsx'
#df1=pd.read_excel(file1)
#df1.rename(columns={'Location on transect (m)':'location_on_trans',\
#                    'Coral Species present (#)':'Coral_species_present'},\
#           inplace=True)
#lat=-18.2057
#lon=177.67
#df1['lat']=lat#-18.2057
#df1['lon']=lon#177.67
#df1.to_csv('../../756580/1/data/frequency.csv',index=False)

### Growth data
file2 = 'Clements and Hay 2019_Nature E&E_Growth Data_Month 4.xlsx'
df2=pd.read_excel(file2)
df2.rename(columns={'Mass Change (%)':'Mass_Change'},inplace=True)
#
file3 = 'Clements and Hay 2019_Nature E&E_Growth Data_Month 16.xlsx'
df3=pd.read_excel(file3)
df3.rename(columns={'Mass Change (%)':'Mass_Change'},inplace=True)
#
df_growth=pd.merge(df2,df3,\
                   on=['Plot','ID','Species','Treatment'],\
                   how='outer',\
                   suffixes=('_Month_4','_Month_16')) # growth data
df_growth['lat']=lat
df_growth['lon']=lon
df_growth.sort_values('Plot',inplace=True)
df_growth.to_csv('../../756532/1/data/growth.csv',index=False) # complete

### density
#file4 = 'Clements and Hay 2019_Nature E&E_Plot Gastropod Densities.xlsx'
#df4=pd.read_excel(file4)
#df4.rename(columns={'Abundance per plot ':'Abundance',\
#                    'Density per plot ':'Density',\
#                    'Biomass (g)':'Biomass',\
#                    'Cover (%)':'Cover'},\
#                     inplace=True)
#df4['lat']=lat
#df4['lon']=lon
#df4.sort_values(['Plot','Species','Treatment'],inplace=True)
#df4.to_csv('density.csv',index=False)


### biomass
#file5 = 'Clements and Hay 2019_Nature E&E_Plot Macroalgal Biomass_Month 16.xlsx'
#df5=pd.read_excel(file5)
#df5.rename(columns={'Abundance per plot ':'Abundance',\
#                    'Density per plot ':'Density',\
#                    'Biomass (g)':'Biomass',\
#                    'Cover (%)':'Cover'},\
#                    inplace=True)
#df5['lat']=lat
#df5['lon']=lon
#df5.sort_values(['Plot','Species','Treatment'],inplace=True)
#df5.to_csv('biomass.csv',index=False)


## cover
#file6 = 'Clements and Hay 2019_Nature E&E_Plot Maroalgal Cover_Month 4.xlsx'
#df6=pd.read_excel(file6)
#df6.rename(columns={'Abundance per plot ':'Abundance',\
#                    'Density per plot ':'Density',\
#                    'Biomass (g)':'Biomass',\
#                    'Cover (%)':'Cover'},\
#                    inplace=True)
#df6['lat']=lat
#df6['lon']=lon
#df6.sort_values(['Plot','Species','Treatment'],inplace=True)
#df6.to_csv('cover.csv',index=False)

#
#df_dc=pd.merge(df4,df5,\
#               on=['Plot','Species','Treatment'],\
#               how='outer') # density & biomass
#df_dcb=pd.merge(df_dc,df6,\
#                on=['Plot','Species','Treatment'],\
#                how='outer') # density, biomass, & cover
#df_dcb['lat']=lat
#df_dcb['lon']=lon
#df_dcb.sort_values(['Plot','Species','Treatment'],inplace=True)
#df_dcb.to_csv('dens_cov_biomass.csv',index=False)
#
### Tissue Mortality
#file7 = 'Clements and Hay 2019_Nature E&E_Tissue Mortality_Month 16.xlsx'
#df7=pd.read_excel(file7)
#df7.rename(columns={'Tissue Mortality (%)':'Tissue_Mortality'},inplace=True)
#
#file8 = 'Clements and Hay 2019_Nature E&E_Tissue Mortality_Month 4.xlsx'
#df8=pd.read_excel(file8)
#df8.rename(columns={'Tissue Mortality (%)':'Tissue_Mortality'},inplace=True)
#
#df_tiss_mort=pd.merge(df7,df8,\
#                      on=['Plot','ID','Species','Treatment'],\
#                      how='outer',\
#                      suffixes=('_Month_16','_Month_4'))
#df_tiss_mort['lat']=lat
#df_tiss_mort['lon']=lon
#df_tiss_mort.sort_values(['Plot','ID','Species'],inplace=True)
#df_tiss_mort.to_csv('tissue_mortality.csv',index=False)
#
#
#
