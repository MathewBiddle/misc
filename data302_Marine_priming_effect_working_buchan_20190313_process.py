import pandas as pd

df = pd.read_excel('Sample_Information_for_JGI_DATA.xlsx',dtype=str)

print(df)
df_transposed=df.T

df_transposed['lat']=31.972
df_transposed['lon']=-81.028

print(df_transposed)
df_transposed.to_csv('Sample_Information_for_JGI_DATA.csv',header=False,index=True)
