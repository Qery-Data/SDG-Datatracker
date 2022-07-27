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

#8.1.1 Annual growth rate of real GDP per capita World (f4NgG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NY_GDP_PCAP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_1_1_Annual_GDP_Growth_Per_Capita_World_Total.csv', index=True)

#8.1.1 Annual growth rate of real GDP per capita SDG Regions (Z2r6Q)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NY_GDP_PCAP.1+53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.loc['2010-2014'] = (df_new.loc[2010]+df_new.loc[2011]+df_new.loc[2012]+df_new.loc[2013]+df_new.loc[2014])/5
df_new.loc['2015-2020'] = (df_new.loc[2015]+df_new.loc[2016]+df_new.loc[2017]+df_new.loc[2018]+df_new.loc[2019]+df_new.loc[2020])/6
df_new = df_new.loc[['2010-2014','2015-2020']]
df_new.to_csv('data/8_1_1_Annual_GDP_Growth_Per_Capita_World_SDG_Regions.csv', index=True)

#8.2.1 Annual growth rate of real GDP per employed person World (gfyRk)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_PCAP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_2_1_Annual_GDP_Growth_Per_Employed_World_Total.csv', index=True)

#8.2.1 Annual growth rate of real GDP per capita SDG Regions (I0aUG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_PCAP.1+53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.loc['2010-2014'] = (df_new.loc[2010]+df_new.loc[2011]+df_new.loc[2012]+df_new.loc[2013]+df_new.loc[2014])/5
df_new.loc['2015-2020'] = (df_new.loc[2015]+df_new.loc[2016]+df_new.loc[2017]+df_new.loc[2018]+df_new.loc[2019]+df_new.loc[2020])/6
df_new = df_new.loc[['2010-2014','2015-2020']]
df_new.to_csv('data/8_2_1_Annual_GDP_Growth_Per_Employed_World_SDG_Regions.csv', index=True)

#8.3.1 Proportion of informal employment in total employment World and SDG regions (IRm9W)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_ISV_IFEM.1+9+53+62+513+747+753+202+419._T........._T./?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 9:'Oceania', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_3_1_Informal_Employment_World_SDG_Regions.csv', index=True)

#8.3.1 Proportion of informal employment in total employment Female and Male World and SDG regions (gdlsv)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_ISV_IFEM.1+9+53+62+513+747+753+202+419.F+M........._T./?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SEX', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 9:'Oceania', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Australia and New Zealand','Latin America and the Caribbean'])
df_new.rename(index={'F':'Female', 'M':'Male'},inplace=True)
df_new.to_csv('data/8_3_1_Informal_Employment_Female_Male_World_SDG_Regions.csv', index=True)

#8.3.1 Proportion of informal employment in total employment Sector World and SDG regions (XDmHe)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_ISV_IFEM.1+9+53+62+513+747+753+202+419._T.........ISIC4_A+ISIC4_BTU./?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='ACTIVITY', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 9:'Oceania',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Australia and New Zealand','Latin America and the Caribbean'])
df_new.rename(index={'ISIC4_A':'Agriculture, forestry and fishing', 'ISIC4_BTU':'Non-agriculture'},inplace=True)
df_new.to_csv('data/8_3_1_Informal_Employment_Sector_World_SDG_Regions.csv', index=True)

#8.4.1 Material footprint World (G1ZDM,DT5Ja,m88Wt)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_MAT_FTPRPC+EN_MAT_FTPRPG+EN_MAT_FTPRTN............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'EN_MAT_FTPRTN':'Material footprint (in millions of tonnes)','EN_MAT_FTPRPG':'Material footprint per unit of GDP','EN_MAT_FTPRPC':'Material footprint (in tonnes) per capita'}, inplace=True)
df_new.to_csv('data/8_4_1_Material_Footprint_World_Total.csv', index=True)

#8.4.2 Domestic material consumption Nordics (UoEQP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_MAT_DOMCMPG.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/8_4_2_Domestic_Material_Consumption_Nordics.csv', index=True)

#8.4.2 Domestic material consumption SDG Regions (CKrtc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_MAT_DOMCMPG.53+62+513+543+747+753+202+419..........._T/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_4_2_Domestic_Material_Consumption_SDG_Regions.csv', index=True)

#8.5.2 Unemployment rate World (IFpK5)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_UEM.1._T.Y_GE15........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_5_2_Unemployment_Rate_World_Total.csv', index=True)

#8.5.2 Unemployment rate sex and age World (lBsRn)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_UEM.1._T.Y15T24+Y_GE25........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='AGE', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'Y15T24':'Youth (15-24)', 'Y_GE25':'Adult (25+)'}, inplace=True)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_UEM.1.F+M.Y_GE15........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new1 = df_csv.pivot(index='SEX', columns='TIME_PERIOD', values='OBS_VALUE')
df_new1.rename(index={'F':'Female', 'M':'Male'}, inplace=True)
df_all = pd.concat([df_new,df_new1], axis=0)
df_all.to_csv('data/8_5_2_Unemployment_Rate_Sex_Age_World_Total.csv', index=True)

#8.5.2 Unemployment rate SDG Regions (7f2NZ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_UEM.53+62+513+543+747+753+202+419._T.Y_GE15........./?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_5_2_Unemployment_Rate_SDG_Regions.csv', index=True)

#8.5.2 Unemployment rate Nordics (lo3xm)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_UEM.208+246+352+578+752._T.Y_GE15........./ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/8_5_2_Unemployment_Rate_Nordics.csv', index=True)

#8.6.1 Youth not in education, employment or training World (eA23i)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_NEET.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_6_1_NEET_World_Total.csv', index=True)

#8.6.1 Youth not in education, employment or training SDG Regions (fn08X)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_NEET.53+62+513+543+747+753+202+419._T........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_6_1_NEET_SDG_Regions.csv', index=True)

#8.6.1 Youth not in education, employment or training by sex SDG Regions (e3hxd)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_NEET.1+53+62+513+543+747+753+202+419.F+M........../?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SEX', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.rename(index={'F':'Female','M':'Male'}, inplace=True)
df_new.to_csv('data/8_6_1_NEET_Sex_SDG_Regions.csv', index=True)

#8.6.1 Youth not in education, employment or training Nordics (6sJ4k)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_NEET.208+246+352+578+752._T........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/8_6_1_NEET_Nordics.csv', index=True)