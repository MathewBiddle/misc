# process.py
# This script reads in semi-standard csv file and writes out a combined file
import glob
import pandas as pd

datafiles=glob.glob("*.csv")
if 'combined.csv' in datafiles:
   datafiles.remove('combined.csv')
dffinal=pd.DataFrame()
for f in datafiles:
   print(f)
   info=pd.read_csv(f,header=None,nrows=9,sep="\n")
   ## parse time
   time = pd.to_datetime(\
     str(info.iloc[8]).split(",")[0].\
     replace("0    # NMEA UTC (Time): ",""))
   ## parse longitude
   lon = str(info.iloc[7]).split(",")[0].\
     replace("0    # NMEA Longitude: ","")
   longitude=float(lon.split(" ")[0])+(float(lon.split(" ")[1])/60)
   if lon.split(" ")[2]=='W':
      longitude=longitude*-1

   ## parse latitude
   lat = str(info.iloc[6]).split(",")[0].\
     replace("0    # NMEA Latitude: ","")
   latitude=float(lat.split(" ")[0])+(float(lat.split(" ")[1])/60)
   if lat.split(" ")[2]=='S':
      latitude=latitude*-1

   ## parse cast
   castid = str(info.iloc[5]).split(",")[0].\
     replace("0    # Cast: ","").split(" ")[0]
   castno = str(info.iloc[5]).split(",")[0].\
     replace("0    # Cast: ","").split(" ")[1].replace("(","")

   ## read data and put header info
   df=pd.read_csv(f,na_values=-9.90E+29,header=10)
   df['time_utc']=time
   df['lon']=longitude
   df['lat']=latitude
   df['cast_id']=castid
   df['cast_no']=castno
   dffinal=pd.concat([dffinal,df])
dffinal.sort_values(['time_utc','depth'],ascending=[True,True],inplace=True)
## write combined data file
dffinal.to_csv('combined.csv',index=False,date_format='%Y-%m-%dT%H:%M:%SZ',float_format="%6.4f")
# write jgofs data comments
import datetime
now = datetime.datetime.now()
f = open('combined.datacomments','w')
lines=[]
lines.append("\# CTD data from AT39-01 (North Pond 2017 expedition)\n")
lines.append("\# PI: Grieg F. Steward\n")
lines.append("\# Version: %s\n" % now.strftime("%Y-%m-%d"))
f.writelines(lines)
f.close()

