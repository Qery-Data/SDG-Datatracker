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

#1.1.1 Extreme Poverty World total (vBtQ6)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SI_POV_DAY1.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new["2019"] = ""
df_new["2020"] = ""
df_new["2021"] = ""
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

#1.1.1 Extreme Poverty SDG Regions
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SI_POV_DAY1.9+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/1_1_1_Extreme_Poverty_World_SDG_Regions.csv', index=True)

#Update DW
chartid = '9hnSw'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.1.1 Extreme Poverty Nordics (QvvA3)
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

#1.2.1 Relative Poverty Nordics
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

#1.2.2 Multidimensional Poverty Nordics (Ko0UR)
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

#1.3.1 Social Protection Coverage World Regions (cb7Xz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SI_COV_BENFTS.1+53+543+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1: 'World', 9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
data_date = str(df_new.columns[0])
df_new.rename(columns={df_new.columns[0]:'Share covered'}, inplace=True)
df_new.to_csv('data/1_3_1_SOC_World_SDG_Regions.csv', index=True)
title_date = 'Share of population covered by at least one social protection cash benefit, by SDG region.' ' Data for ' + data_date
#Update DW
chartid = 'cb7Xz'
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

#1.3.1 Social protection - nine indicators from the ILO, one from the OECD (out of work) Nordics
df_bnfts = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_TOTAL?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_bnfts= df_bnfts.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
bnfts_data_date = df_new_bnfts.index[0]
df_new_bnfts.rename(index={df_new_bnfts.index[0]: "Share of population covered by at least one social protection benefit"}, inplace = True)
df_new_bnfts.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_bnfts['Date'] = bnfts_data_date

df_chld = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_CHILD?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_chld = df_chld.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
chld_data_date = df_new_chld.index[0]
df_new_chld.rename(index={df_new_chld.index[0]: "Share of children/households receiving child/family cash benefit"}, inplace = True)
df_new_chld.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_chld['Date'] = chld_data_date

df_disab = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_DISAB?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_disab = df_disab.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
disab_data_date = df_new_disab.index[0]
df_new_disab.rename(index={df_new_disab.index[0]: "Share of population with severe disabilities receiving disability cash benefit"}, inplace = True)
df_new_disab.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_disab['Date'] = disab_data_date

df_matnl = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_F.SOC_CONTIG_MAT?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_matnl = df_matnl.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
matnl_data_date = df_new_matnl.index[0]
df_new_matnl.rename(index={df_new_matnl.index[0]: "Share of mothers with newborns receiving maternity cash benefit"}, inplace = True)
df_new_matnl.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_matnl['Date'] = matnl_data_date

df_pensn = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_PENSION?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_pensn = df_pensn.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
pensn_data_date = df_new_pensn.index[0]
df_new_pensn.rename(index={df_new_pensn.index[0]: "Share of population above statutory pensionable age receiving a pension"}, inplace = True)
df_new_pensn.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_pensn['Date'] = pensn_data_date

df_poor = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_POOR?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_poor = df_poor.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
poor_data_date = df_new_poor.index[0]
df_new_poor.rename(index={df_new_poor.index[0]: "Share of poor population receiving social assistance cash benefit"}, inplace = True)
df_new_poor.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_poor['Date'] = poor_data_date

df_uemp = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_UNE?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_uemp = df_uemp.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
uemp_data_date = df_new_uemp.index[0]
df_new_uemp.rename(index={df_new_uemp.index[0]: "Share of unemployed persons receiving unemployment cash benefit"}, inplace = True)
df_new_uemp.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_uemp['Date'] = uemp_data_date

df_vuln = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_VULN?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_vuln = df_vuln.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
vuln_data_date = df_new_vuln.index[0]
df_new_vuln.rename(index={df_new_vuln.index[0]: "Share of vulnerable population receiving social assistance cash benefit"}, inplace = True)
df_new_vuln.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_vuln['Date'] = vuln_data_date

df_wkinjry = pd.read_csv('https://www.ilo.org/sdmx/rest/data/ILO,DF_SDG_0131_SEX_SOC_RT/NOR+SWE+DNK+ISL+FIN...SEX_T.SOC_CONTIG_INJ?format=csv&startPeriod=2012-01-01&endPeriod=2022-12-31&lastNObservations=1')
df_new_wkinjry = df_wkinjry.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
wkinjry_data_date = df_new_wkinjry.index[0]
df_new_wkinjry.rename(index={df_new_wkinjry.index[0]: "Share of employed population covered in the event of work injury"}, inplace = True)
df_new_wkinjry.rename(columns={'DNK': 'Denmark', 'FIN': 'Finland', 'ISL': 'Iceland', 'NOR':'Norway', 'SWE':'Sweden'}, inplace = True)
df_new_wkinjry['Date'] = wkinjry_data_date

df_new_out_of_work = pd.DataFrame([{'Denmark': 44, 'Finland': 139, 'Iceland': 36, 'Norway': 23, 'Sweden': 22, 'Date': '2017/2018'}], index = ['Recipients of secondary out-of-work benefits as share of poor w.a.p'])
df_all = pd.concat([df_new_bnfts,df_new_chld,df_new_disab,df_new_matnl,df_new_pensn,df_new_uemp,df_new_poor,df_new_vuln,df_new_wkinjry, df_new_out_of_work], axis=0)
df_all.to_csv('data/1_3_1_SOC_Nordics.csv', index=True)
#Update DW
chartid = 'gg4Oo'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.4.1 Basic Services World (gKqbe)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.1..._T......../ALL/?detail=full&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='SERIES', values='OBS_VALUE')
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_World.csv', index=True)
#Update DW
chartid = 'gKqbe'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.4.1 Basic Services SDG Regions V6VAh (Sanitation) F9QxD (Water)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.9+62+513+747+753+202+419..._T......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_SDG_Regions.csv', index=True)
#Update DW
chartid = 'V6VAh'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)
chartid = 'F9QxD'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.4.1 Basic Services Nordics (0cxyL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.208+246+352+578+752..._T......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_Nordics.csv', index=True)
#Update DW
chartid = '0cxyL'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.5.3 National Strategies Score Nordics (ChM6H)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_DSR_LGRGSR.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SG_DSR_LGRGSR': 'Score of adoption'},inplace=True)
df_new.drop(df_new[df_new['Score of adoption'] <= 0.00].index, inplace = True)
df_new.to_csv('data/1_5_3_National_Strategies_Nordics.csv', index=True)
#Update DW
chartid = 'ChM6H'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.5.3 Local Strategies Share Nordics (q2C40)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_DSR_SILS.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SG_DSR_SILS': 'Share of local governments'},inplace=True)
df_new.drop(df_new[df_new['Share of local governments'] <= 0.00].index, inplace = True)
df_new.to_csv('data/1_5_3_Local_Strategies_Nordics.csv', index=True)
#Update DW
chartid = 'q2C40'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.a.1 ODA Poverty Component (TQgd2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..DC_ODA_POVDLG.208+246+352+578+752............/ALL/?detail=full&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.insert(loc=0, column="Flags", value=[':dk:',':fi:',':is:',':no:',':se:'])
df_new.to_csv('data/1_A_1_ODA_Poverty_Nordics.csv', index=True)
#Update DW
chartid = 'TQgd2'
url = "https://api.datawrapper.de/v3/charts/" + chartid + '/publish/'
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.request("POST", url, headers=headers)

#1.a.2 Public Spending Education Nordics (Zsft2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SD_XPD_ESED.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
data_date = str(df_new.columns[0])
df_new.rename(columns={df_new.columns[0]:'Share of total government spending, education'}, inplace=True)
df_new.to_csv('data/1_A_2_Public_Spending_Education_Nordics.csv', index=True)
title_date = 'Share of total government spending on education.' ' Data for ' + data_date
#Update DW
chartid = 'Zsft2'
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
