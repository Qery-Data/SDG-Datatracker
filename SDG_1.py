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
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SI_POV_DAY1.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/1_1_1_Extreme_Poverty_World_Total.csv', index=True)

#1.1.1 Extreme Poverty SDG Regions
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SI_POV_DAY1.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/1_1_1_Extreme_Poverty_World_SDG_Regions.csv', index=True)

#1.1.1 Extreme Poverty Nordics (QvvA3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SI_POV_DAY1.208+246+352+578+752._T._T._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_1_1_Extreme_Poverty_Nordics.csv', index=True)

#1.2.1 Relative Poverty Nordics
oecd_url='https://stats.oecd.org/SDMX-JSON/data/IDD/DNK+FIN+ISL+NOR+SWE.PVT5A.TOT.CURRENT.METH2012/all?startTime=2004'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df["Value"] = 100*df["Value"]
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/1_2_1_Relative_Income_Poverty_Nordics.csv', index=True)

#1.2.2 Multidimensional Poverty Nordics (Ko0UR)
df_csv = pd.read_csv("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SD_MDP_MUHC.208+246+352+578+752._T._T._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_2_2_Multidimensional_Poverty_Nordics.csv', index=True)

#1.3.1 Social Protection Coverage World Regions (cb7Xz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SI_COV_BENFTS.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
data_date = str(df_new.columns[0])
df_new.rename(columns={df_new.columns[0]:'Share covered'}, inplace=True)
df_new.to_csv('data/1_3_1_SOC_World_SDG_Regions.csv', index=True)

#1.3.1 Social protection - nine indicators from the ILO, one from the OECD (out of work) Nordics
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SI_COV_BENFTS+SI_COV_CHLD+SI_COV_DISAB+SI_COV_LMKT+SI_COV_MATNL+SI_COV_PENSN+SI_COV_POOR+SI_COV_SOCAST+SI_COV_SOCINS+SI_COV_UEMP+SI_COV_VULN+SI_COV_WKINJRY.208+246+352+578+752._T........../ALL/?detail=full&&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SI_COV_BENFTS': 'Share of population covered by at least one social protection benefit', 'SI_COV_CHLD': 'Share of children/households receiving child/family cash benefit', 'SI_COV_DISAB': 'Share of population with severe disabilities receiving disability cash benefit','SI_COV_PENSN':'Share of population above statutory pensionable age receiving a pension','SI_COV_POOR':'Share of poor population receiving social assistance cash benefit','SI_COV_UEMP':'Share of unemployed persons receiving unemployment cash benefit','SI_COV_VULN':'Share of vulnerable population receiving social assistance cash benefit','SI_COV_WKINJRY':'Share of employed population covered in the event of work injury'}, inplace=True)
df_new.to_csv('data/1_3_1_SOC_Nordics.csv', index=True)

#1.4.1 Basic Services World (gKqbe)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.1..._T......../ALL/?detail=full&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='SERIES', values='OBS_VALUE')
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_World.csv', index=True)

#1.4.1 Basic Services SDG Regions V6VAh (Sanitation) F9QxD (Water)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.53+62+513+543+747+753+202+419..._T......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_SDG_Regions.csv', index=True)

#1.4.1 Basic Services Nordics (0cxyL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SP_ACS_BSRVSAN+SP_ACS_BSRVH2O.208+246+352+578+752..._T......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SP_ACS_BSRVH2O': 'Basic drinking water services', 'SP_ACS_BSRVSAN': 'Basic sanitation services'},inplace=True)
df_new.to_csv('data/1_4_1_Basic_Services_Nordics.csv', index=True)

#1.5.1 Number of deaths and missing persons due to disasters Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_DSR_MTMP.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_5_1_Deaths_Missing_Persons_Disasters_Nordics.csv', index=True)

#1.5.2 Direct economic loss attributed to disasters as share of GDP Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VS_DSR_LSGP.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_5_2_Direct_Economic_Loss_Share_GDP_Nordics.csv', index=True)

#1.5.3 National Strategies Score Nordics (ChM6H)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DSR_LGRGSR.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SG_DSR_LGRGSR': 'Score of adoption'},inplace=True)
df_new.drop(df_new[df_new['Score of adoption'] <= 0.00].index, inplace = True)
df_new.to_csv('data/1_5_3_National_Strategies_Nordics.csv', index=True)

#1.5.4 Local Strategies Share Nordics (q2C40)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DSR_SILS.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'SG_DSR_SILS': 'Share of local governments'},inplace=True)
df_new.drop(df_new[df_new['Share of local governments'] <= 0.00].index, inplace = True)
df_new.to_csv('data/1_5_4_Local_Strategies_Nordics.csv', index=True)

#1.a.1 ODA Poverty Component (TQgd2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..DC_ODA_POVDLG.208+246+352+578+752............/ALL/?detail=full&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/1_a_1_ODA_Poverty_Nordics.csv', index=True)

#1.a.2 Public Spending Education Nordics (Zsft2)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SD_XPD_ESED.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
data_date = str(df_new.columns[0])
df_new.rename(columns={df_new.columns[0]:'Share of total government spending, education'}, inplace=True)
df_new.to_csv('data/1_a_2_Public_Spending_Education_Nordics.csv', index=True)