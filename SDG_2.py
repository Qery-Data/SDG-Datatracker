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

#2.1.1 Prevalence of undernourishment % World (2my6k)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_ITK_DEFC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/2_1_1_Prevalence_Undernourishment_World_Total_%.csv', index=True)
#Update DW
chartid = '2my6k'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.1 Prevalence of undernourishment number World (OLyOp)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_ITK_DEFCN.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/2_1_1_Prevalence_Undernourishment_World_Total.csv', index=True)
#Update DW
chartid = 'OLyOp'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.1 Prevalence of undernourishment % SDG Regions (A4Tib)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_ITK_DEFC.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_1_1_Prevalence_Undernourishment_SDG_Regions_%.csv', index=True)
#Update DW
chartid = 'A4Tib'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.1 Prevalence of undernourishment number SDG Regions (XMsfz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_ITK_DEFCN.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_1_1_Prevalence_Undernourishment_SDG_Regions.csv', index=True)
#Update DW
chartid = 'XMsfz'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.2 Prevalence of moderate or severe food insecurity % World (xVpsa)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESMS.1._T.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/2_1_2_Prevalence_Mod_Sev_Food_Ins_World_%.csv', index=True)
#Update DW
chartid = 'xVpsa'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.2 Prevalence of moderate or severe food insecurity number World (778M0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESMSN.1._T.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/2_1_2_Prevalence_Mod_Sev_Food_Ins_World.csv', index=True)
#Update DW
chartid = '778M0'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.2 Prevalence of moderate or severe food insecurity % SDG Regions (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESMS.9+62+513+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_1_2_Prevalence_Mod_Sev_Food_Ins_SDG_Regions_%.csv', index=True)
#Update DW
chartid = 'xxxxx'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.2 Prevalence of moderate or severe food insecurity number SDG Regions (PfO0n)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESMSN.9+62+513+747+753+202+419._T.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
data_date = str(df_new.index[0])
df_new.rename(index={df_new.index[0]: "Moderate or severe"}, inplace = True)

df_csv2 = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESSN.9+62+513+747+753+202+419._T.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new2 = df_csv2.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new2.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new2.rename(index={df_new2.index[0]: "Severe"}, inplace = True)

df_all = pd.concat([df_new,df_new2], axis=0)
df_all.loc['Moderate'] = df_all.diff(-1).dropna().values.tolist()[0]
df_all.drop(['Moderate or severe'], inplace=True)
df_all.to_csv('data/2_1_2_Prevalence_Mod_Sev_Food_Ins_SDG_Regions.csv', index=True)
title_date = 'Number of people (million) who are moderately or severely food insecure*.' ' Data for ' + data_date
#Update DW
chartid = 'PfO0n'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/'
payload = {"metadata": {"describe": {"intro": title_date}}}
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*",
    "Content-Type": "application/json"
    }
response = requests.request("PATCH", url, json=payload, headers=headers)
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.1.2 Prevalence of moderate or severe food insecurity % Nordics (RGtq1)
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..AG_PRD_FIESMS.208+246+352+578+752._T............/ALL/?detail=full&startPeriod=1967-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/2_1_2_Prevalence_Mod_Sev_Food_Ins_Nordics_%.csv', index=True)
#Update DW
chartid = 'RGtq1'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.1 Prevalence of stunting % World (JvlHe)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_STNT.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2025"] = ""
df_new["2030"] = ""
df_new.to_csv('data/2_2_1_Prevalence_Stunting_World_Total_%.csv', index=True)
#Update DW
chartid = 'JvlHe'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.1 Prevalence of stunting % SDG Regions (2cgDy)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_STNT.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_2_1_Prevalence_Stunting_SDG_Regions_%.csv', index=True)
#Update DW
chartid = '2cgDy'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Prevalence of wasting % World (FMKn3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_WAST.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2025"] = 5
df_new["2030"] = 3
df_new.to_csv('data/2_2_2_Prevalence_Wasting_World_Total_%.csv', index=True)
#Update DW
chartid = 'FMKn3'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Prevalence of overweight % World (5y7LP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_STA_OVWGT.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2030"] = ""
df_new.to_csv('data/2_2_2_Prevalence_Overweight_World_Total_%.csv', index=True)
#Update DW
chartid = '5y7LP'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Prevalence of overweight % SDG Regions (2hoyZ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SN_STA_OVWGT.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_2_2_Prevalence_Overweight_SDG_Regions_%.csv', index=True)
#Update DW
chartid = '2hoyZ'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Prevalence of anaemia  % World (z6Gaf)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_ANEM.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2030"] = ""
df_new.to_csv('data/2_2_2_Prevalence_Anaemia_World_Total_%.csv', index=True)
#Update DW
chartid = 'z6Gaf'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Prevalence of anaemia % SDG Regions (Xk0pL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_ANEM.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/2_2_2_Prevalence_Anaemia_SDG_Regions_%.csv', index=True)
#Update DW
chartid = 'Xk0pL'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#2.2.2 Obesity Rate Nordics (OECD)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_LVNG/BODYOBMS.TOTPOPTX.FIN/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Country', columns='Year', values='Value')

oecd_url2='https://stats.oecd.org/SDMX-JSON/data/HEALTH_LVNG/BODYOBSR.TOTPOPTX.DNK+ISL+NOR+SWE/all?startTime=2000'
result2 = requests.get(oecd_url2, headers={'Accept': 'text/csv'})
df2=pd.read_csv(io.StringIO(result2.text))
df_new2 = df2.pivot(index='Country', columns='Year', values='Value')

df_all = pd.concat([df_new2,df_new], axis=0)
df_all.to_csv('data/2_2_2_Prevalence_Obesity_Nordics_%.csv', index=True)
#Update DW
chartid = 'xxxxx'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)
