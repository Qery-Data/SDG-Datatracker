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

#7.1.1 Proportion of population with access to electricity World (Uuvw0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_ACS_ELEC.1..._T......../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/7_1_1_Access_Electricity_World_Total.csv', index=True)

#7.1.1 Proportion of population with access to electricity SDG Regions (X0IBY)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_ACS_ELEC.53+62+513+543+747+753+202+419..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/7_1_1_Access_Electricity_SDG_Regions.csv', index=True)

#7.1.1 Proportion of population with access to electricity Urban Rural SDG Regions (1AwOS)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_ACS_ELEC.1+53+62+513+543+747+753+202+419...U+R......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='URBANISATION', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.rename(index={'U':'Urban','R':'Rural'},inplace=True)
df_new.to_csv('data/7_1_1_Access_Electricity_Urban_Rural_World_SDG_Regions.csv', index=True)

#7.1.1 Proportion of population with access to electricity Nordics (ksngG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_ACS_ELEC.208+246+352+578+752...U+R......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='URBANISATION', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'U':'Urban','R':'Rural'},inplace=True)
df_new.to_csv('7_1_1_Access_Electricity_Urban_Rural_Nordics.csv', index=True)
df_new.to_csv('data/7_1_1_Access_Electricity_Urban_Rural_Nordics.csv', index=True)

#7.1.2 Proportion of population primary reliance on clean fuels and technology World (dE3Ri)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_EGY_CLEAN.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/7_1_2_Clean_Fuels_Technology_World_Total.csv', index=True)

#7.1.2 Proportion of population primary reliance on clean fuels and technology SDG Regions (kFqpw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_EGY_CLEAN.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/7_1_2_Clean_Fuels_Technology_SDG_Regions.csv', index=True)

#7.2.1 Renewable energy share in the total final energy consumption World (JYmiU)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_FEC_RNEW.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/7_2_1_Renewable_Energy_Share_World_Total.csv', index=True)

#7.2.1 Renewable energy share in the total final energy consumption SDG Regions (WYLTV)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_FEC_RNEW.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/7_2_1_Renewable_Energy_Share_SDG_Regions.csv', index=True)

#7.2.1 Renewable energy share in the total final energy consumption Nordics (iH0RT)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_FEC_RNEW.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/7_2_1_Renewable_Energy_Share_Nordics.csv', index=True)

#7.2.1 Renewable electricity share in the total electricity generation Nordics (MG14f)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/GREEN_GROWTH/DNK+FIN+ISL+NOR+SWE+OECD.RE_NRG/all?startTime=2000&endTime=2021'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/7_2_1_Renewable_Electricity_Share_Nordics.csv', index=True)

#7.3.1 Energy intensity level of primary energy World (4A6F5)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_EGY_PRIM.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/7_3_1_Energy_Intensity_World_Total.csv', index=True)

#7.3.1 Energy intensity level of primary energy SDG Regions (kry7k)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_EGY_PRIM.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/7_3_1_Energy_Intensity_SDG_Regions.csv', index=True)

#7.3.1  Energy intensity level of primary energy Nordics (45Br2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_EGY_PRIM.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/7_3_1_Energy_Intensity_Nordics.csv', index=True)