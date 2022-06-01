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

#3.1.1 Maternal mortlity ratio World (GSN09)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_MORT.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2030"] = ""
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_World_Total.csv', index=True)
#Update DW
chartid = 'GSN09'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Maternal mortlity ratio SDG regions (ldsu3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_MORT.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_SDG_Regions.csv', index=True)
#Update DW
chartid = 'ldsu3'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Maternal mortality ratio Nordics (OECD) (w7m0C) 
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_STAT/MATIMATM.TXCMMMTX.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.insert(loc=0, column="Flags", value=[':dk:',':fi:',':is:',':no:',':se:'])
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_Nordics.csv', index=True)
#Update DW
chartid = 'w7m0C'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Delivery coverage World (PURO4)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_BRTC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_World_Total.csv', index=True)
#Update DW
chartid = 'PURO4'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Delivery coverage World (PURO4)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_BRTC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_World_Total.csv', index=True)
#Update DW
chartid = 'PURO4'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Delivery coverage SDG regions (Nyj1B)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_BRTC.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_DETAIL', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_SDG_Regions.csv', index=True)
#Update DW
chartid = 'Nyj1B'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.1.1 Delivery coverage Nordics (ax3MB)
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_BRTC.208+246+352+578+752............../ALL/?detail=full&startPeriod=1967-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_Nordics.csv', index=True)
#Update DW
chartid = 'ax3MB'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.2.1 Child mortality (under 5 years) World (nlIg9)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_DYN_MORT.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2030"] = ""
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_World_Total.csv', index=True)
#Update DW
chartid = 'nlIg9'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.2.1 Child mortality (under 5 years) SDG regions (cjeVd)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_DYN_MORT.9+62+513+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_SDG_Regions.csv', index=True)
#Update DW
chartid = 'cjeVd'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#3.2.1 Child mortality (under 5 years) Nordics (VDUy3)
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_DYN_MORT.208+246+352+578+752._T........../ALL/?detail=full&startPeriod=1967-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_Nordics.csv', index=True)
#Update DW
chartid = 'VDUy3'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)