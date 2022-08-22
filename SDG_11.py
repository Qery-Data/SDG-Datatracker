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

#11.1.1 Proportion of urban population living in slums World (1Cxh2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_LND_SLUM.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/11_1_1_Share_Urban_Population_Slums_World_Total.csv', index=True)

#11.1.1 Proportion of urban population living in slums SDG Regions (8IGoc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_LND_SLUM.9+62+513+53+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 9: 'Oceania', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/11_1_1_Share_Urban_Population_Slums_SDG_Regions.csv', index=True)

#11.1.1 Overcrowding rate Nordics (krzd4)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HSL/DNK+FIN+ISL+NOR+SWE.DEP.3_1.CWB.TOT.TOT.TOT/all?startTime=2002'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Time', columns='Country', values='Value')
df_new.to_csv('data/11_1_1_Overcrowding_Rate_Nordics.csv', index=True)

#11.2.1 Proportion of population with convenient access to public transport World and SDG regions (tHYxl)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SP_TRN_PUBL.1+9+62+513+53+747+753+202+419......._T..../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 9: 'Oceania', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/11_2_1_Share_Public_Transport_Convenient_Access_World_SDG_Regions.csv', index=True)

#11.6.1 Material recovery rate of municipal waste (recycling and composting) Nordics (qpGLe)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/MUNW/DNK+FIN+ISL+NOR+SWE.MAT_RECOV_SHARE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/11_6_1_Material_Recovery_Rate_Nordics.csv', index=True)

#11.6.2 Mean population exposure to PM2.5 in metropolitan areas Nordics (3hWqR)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/EXP_PM2_5/DNK+FIN+ISL+NOR+SWE.TOTAL.TOTAL.PWM_EX/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/11_6_2_Mean_Exposure_PM25_Metropolititan_Areas_Nordics.csv', index=True)