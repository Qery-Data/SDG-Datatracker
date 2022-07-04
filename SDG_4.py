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

#4.1.1 Proficiency level Lower Secondary Maths Nordics (xnVAf)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_PRFL.208+246+352+578+752._T....ISCED11_2...SKILL_MATH.../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower_Maths_Nordics.csv', index=True)

#4.1.1 Proficiency level Lower Secondary Reading Nordics (u5whA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_PRFL.208+246+352+578+752._T....ISCED11_2...SKILL_MATH.../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower_Reading_Nordics.csv', index=True)

#4.1.2 Completion rate World (85zYy)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.1._T....ISCED11_1+ISCED11_2+ISCED11_3....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='EDUCATION_LEV', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/4_1_2_Completion_Rate_World_Total.csv', index=True)

#4.1.2 Completion rate primary SDG Regions (Nwau1)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.9+62+513+747+753+202+419._T....ISCED11_1....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/4_1_2_Completion_Rate_Primary_SDG_Regions.csv', index=True)

#4.1.2 Completion rate lower secondary SDG Regions (siE3p)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.9+62+513+747+753+202+419._T....ISCED11_2....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/4_1_2_Completion_Rate_Lower_Secondary_SDG_Regions.csv', index=True)

#4.1.2 Completion rate upper secondary SDG Regions (oMLtb)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.9+62+513+747+753+202+419._T....ISCED11_3....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/4_1_2_Completion_Rate_Upper_Secondary_SDG_Regions.csv', index=True)

#4.1.1 Proficiency level Lower Secondary Maths Nordics (xnVAf)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_PRFL.208+246+352+578+752._T....ISCED11_2...SKILL_MATH.../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower__Secondary_Maths_Nordics.csv', index=True)

#4.1.1 Proficiency level Lower Secondary Reading Nordics (u5whA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_PRFL.208+246+352+578+752._T....ISCED11_2...SKILL_MATH.../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower_Secondary_Reading_Nordics.csv', index=True)

#4.1.2 Completion rate Lower Secondary Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.208+246+352+578+752._T.._T._T.ISCED11_2....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_2_Completion_Rate_Lower_Secondary_Nordics.csv', index=True)

#4.1.2 Completion rate Upper Secondary Nordics (AzWOZ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.208+246+352+578+752._T.._T._T.ISCED11_3....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_2_Completion_Rate_Upper_Secondary_Nordics.csv', index=True)