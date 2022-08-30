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

#13.1.1 Total greenhouse gas emissions Nordics (hAsML)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/AIR_GHG/DNK+FIN+ISL+NOR+SWE.GHG.TOTAL/all?startTime=1990'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/13_1_1_Total_Greenhouse_Gas_Emissions_Nordics.csv', index=True)

#13.1.1 Total greenhouse gas emissions per capita Nordics (V6Zeh)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/AIR_GHG/DNK+FIN+ISL+NOR+SWE.GHG.GHG_CAP/all?startTime=1990'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/13_1_1_Total_Greenhouse_Gas_Emissions_Capita_Nordics.csv', index=True)

#13.1.1 Total greenhouse gas emissions per unit of GDP Nordics (6xFUZ)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/AIR_GHG/DNK+FIN+ISL+NOR+SWE.GHG.GHG_GDP/all?startTime=1990'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/13_1_1_Total_Greenhouse_Gas_Emissions_Unit_GDP_Nordics.csv', index=True)
