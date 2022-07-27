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
