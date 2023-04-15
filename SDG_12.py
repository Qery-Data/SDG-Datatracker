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

#12.1.1 Number of countries with SCP policies World and SDG regions (ke52o)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_SCP_CNTRY.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/12_1_1_Countries_SCP_World_SDG_Regions.csv', index=True)

#12.1.1 Number of SCP policies World and SDG regions (UM9DY)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_SCP_TOTLN.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/12_1_1_Number_SCP_Policies_World_SDG_Regions.csv', index=True)

#12.1.1 Number of countries with SCP policies Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_SCP_CNTRY.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/12_1_1_SCP_Policies_Nordics.csv', index=True)

#12.3.1 Food loss World and SDG regions (SZ9S3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..AG_FLS_PCT.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/12_3_1_Food_Loss_World_SDG_Regions.csv', index=True)

#12.3.1 Food waste Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..AG_FOOD_WST_PC.208+246+352+578+752........FWS_RTL+FWS_OOHC+FWS_HHS.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='COMPOSITE_BREAKDOWN', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'FWS_HHS': 'Households', 'FWS_OOHC': 'Out-of-home consumption', 'FWS_RTL': 'Retail'}, inplace=True)
df_new.to_csv('data/12_3_1_Food_Waste_Nordics.csv', index=True)

#12.4.1 International multilateral environmental agreements World and SDG regions (6DgqI)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_HAZ_CMRBASEL+SG_HAZ_CMRMNTRL+SG_HAZ_CMRROTDAM+SG_HAZ_CMRSTHOLM+SG_HAZ_CMRMNMT.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'SG_HAZ_CMRBASEL': 'Basel Convention', 'SG_HAZ_CMRMNTRL': 'Montreal Protocol', 'SG_HAZ_CMRROTDAM': 'Rotterdam Convention', 'SG_HAZ_CMRSTHOLM': 'Stockholm Convention'}, inplace=True)
df_new.to_csv('data/12_4_1_International_Environmental_Agreements_World_SDG_Regions.csv', index=True)

#12.4.2 E-waste collection rate World and SDG regions (3P5Co)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..EN_EWT_COLLR.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.insert(7, "World", [0.228])
df_new =df_new*100
df_new.to_csv('data/12_4_2_E-waste_Collection_Rate_World_SDG_Regions.csv', index=True)

#12.4.1 International multilateral environmental agreements Nordics (ss13G)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_HAZ_CMRBASEL+SG_HAZ_CMRMNTRL+SG_HAZ_CMRROTDAM+SG_HAZ_CMRSTHOLM+SG_HAZ_CMRMNMT.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SG_HAZ_CMRBASEL': 'Basel Convention', 'SG_HAZ_CMRMNTRL': 'Montreal Protocol', 'SG_HAZ_CMRROTDAM': 'Rotterdam Convention', 'SG_HAZ_CMRSTHOLM': 'Stockholm Convention','SG_HAZ_CMRMNMT':'Minamata Convention'}, inplace=True)
df_new.to_csv('data/12_4_1_International_Environmental_Agreements_Nordics.csv', index=True)

#12.6.1 Number of companies publishing sustainability reports World (QECBI)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..EN_SCP_FRMN.1.........._T./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/12_6_1_Companies_Sustainability_Reports_World_Total.csv', index=True)

#12.6.1 Number of companies publishing sustainability reports SDG regions (E6NpQ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..EN_SCP_FRMN.53+62+513+543+747+753+202+419.........._T./ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/12_6_1_Companies_Sustainability_Reports_SDG_Regions.csv', index=True)

#12.6.1 Number of companies publishing sustainability reports Nordics (bJjPu)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..EN_SCP_FRMN.208+246+352+578+752.........._T./ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/12_6_1_Companies_Sustainability_Reports_Nordics.csv', index=True)

#12.7.1 Number of countries implementing sustainable public procurement policies Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_SCP_PROCN+SG_SCP_PROCN_HS+SG_SCP_PROCN_LS.208+246+352+578+752......._T.DEG_LOW+DEG_MLOW.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SG_SCP_PROCN': 'Yes'}, inplace=True)
df_new.to_csv('data/12_7_1_Sustainable_Public_Procurement_Nordics.csv', index=True)

#12.c.1 Fossil fuel subsidies as share of GDP World (T7Yda)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..ER_FFS_CMPT_GDP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/12_c_1_Fossil_Fuel_Share_GDP_World_Total.csv', index=True)

#12.c.1 Fossil fuel subsidies as share of GDP SDG regions (knu86)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..ER_FFS_CMPT_GDP.53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/12_c_1_Fossil_Fuel_Share_GDP_SDG_Regions.csv', index=True)

#12.c.1 Fossil fuel subsidies as share of GDP Nordics (7uni3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..ER_FFS_CMPT_GDP.208+246+352+578+752.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SG_SCP_PROCN': 'Yes'}, inplace=True)
df_new.to_csv('data/12_c_1_Fossil_Fuel_Share_GDP_Nordics.csv', index=True)