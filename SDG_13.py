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

#13.2.2 Total greenhouse gas emissions Nordics (hAsML)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..EN_ATM_GHGT_AIP.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/13_2_2_Total_Greenhouse_Gas_Emissions_Nordics.csv', index=True)

#13.2.2 Total greenhouse gas emissions per capita Nordics (V6Zeh)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/AIR_GHG/DNK+FIN+ISL+NOR+SWE.GHG.GHG_CAP/all?startTime=1990'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/13_2_2_Total_Greenhouse_Gas_Emissions_Capita_Nordics.csv', index=True)

#13.2.2 Total greenhouse gas emissions per unit of GDP Nordics (6xFUZ)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/AIR_GHG/DNK+FIN+ISL+NOR+SWE.GHG.GHG_GDP/all?startTime=1990'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/13_2_2_Total_Greenhouse_Gas_Emissions_Unit_GDP_Nordics.csv', index=True)
