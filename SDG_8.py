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

#8.4.2 Domestic material consumption GDP SDG Regions (CKrtc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_MAT_DOMCMPG.53+62+513+543+747+753+202+419..........._T/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_4_2_Domestic_Material_Consumption_GDP_SDG_Regions.csv', index=True)

#8.4.2 Domestic material consumption share SDG Regions (CKrtc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_MAT_DOMCMPT.53+62+513+543+747+753+202+419..........._T/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_4_2_Domestic_Material_Consumption_Share_SDG_Regions.csv', index=True)

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
oecd_url='https://stats.oecd.org/SDMX-JSON/data/LFS_SEXAGE_I_R/DNK+FIN+ISL+NOR+SWE.MW.1564.UR.A/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Time', columns='Country', values='Value')
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

#8.7.1 Proportion of children engaged in economic activity and household chores World (JzZVA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_CHLDEC.1+62+513+747+753+202+419._T+F+M........../?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SEX', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Latin America and the Caribbean'])
df_new.rename(index={'_T':'Total','F':'Female','M':'Male'}, inplace=True)
df_new.to_csv('data/8_7_1_Child_Labour_World_SDG_Regions.csv', index=True)

#8.8.1 Fatal occupational injuries Nordics (S5XAa)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_FTLINJUR.208+246+352+578+752._T......._T.../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new = df_new.drop('Iceland', axis=1)
df_new = df_new.loc[[2000,2015]]
df_new.to_csv('data/8_8_1_Fatal_Occupational_Injuries_Nordics.csv', index=True)

#8.8.1 Non-fatal occupational injuries Nordics (kcD6p)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_INJUR.208+246+352+578+752._T......._T.../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new = df_new.drop('Iceland', axis=1)
df_new = df_new.loc[[2000,2015]]
df_new.to_csv('data/8_8_1_Non_Fatal_Occupational_Injuries_Nordics.csv', index=True)

#8.8.2 Level of national compliance with labour rights World and SDG Regions (h8kWB)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_LBR_NTLCPL.1+53+62+513+543+747+35+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 35: 'South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new = df_new.loc[[2015,2020]]
df_new.to_csv('data/8_8_2_Level_Complicance_Labour_Rights_World_SDG_Regions.csv', index=True)

#8.8.2 Level of national compliance with labour rights Nordics (6mUct)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_LBR_NTLCPL.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new = df_new.loc[[2015,2020]]
df_new.to_csv('data/8_8_2_Level_Complicance_Labour_Rights_Nordics.csv', index=True)

#8.9.1 Tourism as share of GDP World (HT2y5)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ST_GDP_ZS.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_9_1_Tourism_Share_GDP_World_Total.csv', index=True)

#8.9.1 Tourism as share of GDP SDG Regions (Xd5MT)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ST_GDP_ZS.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/8_9_1_Tourism_Share_GDP_SDG_Regions.csv', index=True)

#8.9.1 Tourism as share of GDP Nordics (VaHj8)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ST_GDP_ZS.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2010-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/8_9_1_Tourism_Share_GDP_Nordics.csv', index=True)

#8.10.1 Number of commercial bank branches and ATMs per 100,000 adults1 World (7oWLv)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FB_ATM_TOTL+FB_CBK_BRCH.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.rename(index={'FB_CBK_BRCH':'Commercial bank branches', 'FB_ATM_TOTL':'ATMs'},inplace=True)
df_new.to_csv('data/8_10_1_Bank_ATM_World_Total.csv', index=True)

#8.10.2 Share of adults account at a bank/other financial institution/mobile-money-service provider World (89Y58)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FB_BNK_ACCSS.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_10_2_Share_Account_World_Total.csv', index=True)

#8.10.2 Share of adults account at a bank/other financial institution/mobile-money-service provider SDG Regions (di2NN)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FB_BNK_ACCSS.53+62+513+543+747+753+202+419._T........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new = df_new.drop('Oceania*', axis=1)
df_new.to_csv('data/8_10_2_Share_Account_SDG_Regions.csv', index=True)

#8.10.2 Share of adults account at a bank/other financial institution/mobile-money-service provider Nordics (3StXp)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FB_BNK_ACCSS.208+246+352+578+752._T........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/8_10_2_Share_Account_GDP_Nordics.csv', index=True)

#8.a.1 Aid for Trade commitments World (w5PoT)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..DC_TOF_TRDCML.515.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/8_a_1_Aid_For_Trade_World_Total.csv', index=True)

#8.b.1 Youth Employment Strategies World (juFOE)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_CPA_YEMP............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new = df_new[2021].value_counts()
df_new.rename({3.0:'Operationalised',2.0:'Developed and adopted',1.0:'In the process',0:'No developed'}, inplace=True)
df_new.to_csv('data/8_b_1_Youth_Employment_Strategies_World_Total.csv', index=True)