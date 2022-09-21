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

#15.1.1 Forest area as a share of total land area World and SDG regions (5qqbo)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..AG_LND_FRST.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Pct.change'] = (df_new.loc[2020] - df_new.loc[2000])/df_new.loc[2000]*100
df_new.to_csv('data/15_1_1_Forest_Area_Share_Total_Land_Area_World_SDG_Regions.csv', index=True)

#15.1.1 Forest area as a share of total land area Nordics (ZQzSJ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..AG_LND_FRST.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_1_1_Forest_Area_Share_Total_Land_Area_Nordics.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas World (DZflH)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_PTD_FRHWTR+ER_PTD_TERR.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_World_Total.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas World and SDG regions (Pqi7o)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_PTD_FRHWTR+ER_PTD_TERR.53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_SDG_Regions.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas Nordics (Msunw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_PTD_TERR+ER_PTD_FRHWTR.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_Nordics.csv', index=True)