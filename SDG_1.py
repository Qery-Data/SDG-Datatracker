from pyjstat import pyjstat
import requests
import os
import json
from datetime import datetime
import locale
import pandas as pd
os.makedirs('data', exist_ok=True)
access_token = os.getenv('DW_TOKEN')

#1.1 Extreme Poverty World total (vBtQ6)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SI_POV_DAY1.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2030"] = ""
df_new.to_csv('data/1_1_1_Extreme_Poverty_World_Total.csv', index=True)
#Update DW
chartid = 'vBtQ6'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.1 Extreme Poverty Nordics 
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SI_POV_DAY1.208+246+352+578+752._T._T._T......../ALL/?detail=full&startPeriod=1967-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.insert(loc=0, column="Flags", value=[':dk:',':fi:',':is:',':no:',':se:'])
df_new.to_csv('data/1_1_1_Extreme_Poverty_Nordics.csv', index=True)
#Update DW
chartid = 'QvvA3'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.2.1 Relative poverty Nordics
oecd_url='https://stats.oecd.org/SDMX-JSON/data/IDD/DNK+FIN+ISL+NOR+SWE.PVT5A.TOT.CURRENT.METH2012/all?startTime=2004'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df["Value"] = 100*df["Value"]
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/1_2_1_Relative_Income_Poverty_Nordics.csv', index=True)
#Update DW
chartid = 'ix6FV'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.2.2 Multidimensional poverty Nordics
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SD_MDP_MUHC.208+246+352+578+752._T._T._T......../ALL/?detail=full&startPeriod=1967-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_2_2_Multidimensional_Poverty_Nordics.csv', index=True)
#Update DW
chartid = 'Ko0UR'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)