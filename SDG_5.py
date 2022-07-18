from pyjstat import pyjstat
import requests
import os
import json
from datetime import datetime
import locale
import io
import pandas as pd
os.makedirs('data', exist_ok=True)
access_token = os.getenv('DW_TOKEN')

#5.1.1 Legal frameworks SDG Regions (zv9jZ)
#Area 1 overarching legal frameworks and public life
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQLFP.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_1 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_1.rename(index={2020: 'Area 1: Overarching legal frameworks and public life'},inplace=True)
#Area 2 violence against women
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQVAW.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_2 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_2.rename(index={2020: 'Area 2:  Violence against women'},inplace=True)
#Area 3 employment and economic benefits
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQEMP.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_3 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_3.rename(index={2020: 'Area 3: Employment and economic benefits'},inplace=True)
#Area 4 marriage and family
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQMAR.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_4 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_4.rename(index={2020: 'Area 4: Marriage and family'}, inplace=True)
df_all = pd.concat([df_new_area_1,df_new_area_2,df_new_area_3,df_new_area_4], axis=0)
df_all.to_csv('data/5_1_1_Legal_Frameworks_SDG_Regions.csv', index=True)

#5.1.1 Legal frameworks Nordics (IvDU9)
#Area 1 overarching legal frameworks and public life
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQLFP.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_1 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_1.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_1.rename(index={2020: 'Area 1: Overarching legal frameworks and public life'},inplace=True)
#Area 2 violence against women
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQVAW.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_2 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_2.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_2.rename(index={2020: 'Area 2:  Violence against women'},inplace=True)
#Area 3 employment and economic benefits
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQEMP.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_3 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_3.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_3.rename(index={2020: 'Area 3: Employment and economic benefits'},inplace=True)
#Area 4 marriage and family
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQMAR.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_4 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_4.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_4.rename(index={2020: 'Area 4: Marriage and family'}, inplace=True)
df_all = pd.concat([df_new_area_1,df_new_area_2,df_new_area_3,df_new_area_4], axis=0)
df_all.to_csv('data/5_1_1_Legal_Frameworks_Nordics.csv', index=True)

#5.2.1 Violence women SDG Regions (L0gR0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..VC_VAW_MARR.1+150+15+21+53+30+34+35+143+145+202+419+543..Y_GE15........./ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 150:'Europe', 15:'Northern Africa', 21:'Northern America', 53:'Australia and New Zeland',30:'Eastern Asia',34:'Southern Asia',35:'South-Eastern Asia', 143:'Central Asia', 145:'Western Asia',202:'Sub-Saharan Africa', 419:'Latin America and the Caribbean', 543:'Oceania (exc. Australia and New Zealand)'},inplace=True)
df_new.to_csv('data/5_2_1_Violence_Women_SDG_Regions.csv', index=True)

#5.2.1 Violence women Nordics (bKbpd)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..VC_VAW_MARR.208+246+352+578+752..Y_GE15........./ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/5_2_1_Violence_Women_Nordics.csv', index=True)

#5.3.1 Women married union before age 15 18 World (NFYU3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF18.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new_18 = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new_18.rename(index={1:'Before 18'}, inplace=True)
df_all = pd.concat([df_new_15,df_new_18], axis=0)
df_all.to_csv('data/5_3_1_Women_Married_Union_15_18_World_Total.csv', index=True)

#5.3.1 Women married union before age 15 SDG Regions (wBfDz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF15.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/5_3_1_Women_Married_Union_15_SDG_Regions.csv', index=True)

#5.3.1 Women married union before age 18 SDG Regions (seBtO)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF18.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/5_3_1_Women_Married_Union_15_SDG_Regions.csv', index=True)

#5.3.2 Female genital mutilation/cutting Regions (GQN6n)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_FGMS.15+202.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={15: 'Northern Africa', 202: 'Sub-Saharan Africa'},inplace=True)
df_new.to_csv('data/5_3_2_Female_Genital_Mutilation_Cutting_Regions.csv', index=True)

#5.3.2 FGM legal protection Nordics (84qt0)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/GIDDB2019/ALL.DNK+FIN+ISL+NOR+SWE.AIC.RPI_FGM_LAW/all?startTime=2019&endTime=2019'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/5_3_2_FGM_Legal_Protection_Nordics.csv', index=True)