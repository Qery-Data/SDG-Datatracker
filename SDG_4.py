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
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower_Secondary_Maths_Nordics.csv', index=True)

#4.1.1 Proficiency level Lower Secondary Reading Nordics (u5whA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_PRFL.208+246+352+578+752._T....ISCED11_2...SKILL_MATH.../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_1_Proficiency_Level_Lower_Secondary_Reading_Nordics.csv', index=True)

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

#4.1.2 Completion rate Upper Secondary Nordics (AzWOZ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TOT_CPLR.208+246+352+578+752._T.._T._T.ISCED11_3....../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_1_2_Completion_Rate_Upper_Secondary_Nordics.csv', index=True)

#4.2.1 Children developmentally on track (GERZS)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_DEV_ONTRK.1+35+145+202+722._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 35: 'South-Eastern Asia', 145: 'Western Asia', 202: 'Sub-Saharan Africa', 722: 'Small island developing States'},inplace=True)
df_new.to_csv('data/4_2_1_Children_Developmentally_World__Region_Total.csv', index=True)

#4.2.2 Participation rate organised learning children World (vWocC)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_PRE_PARTN.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/4_2_2_Participation_Rate_Learning_Children_World_Total.csv', index=True)

#4.2.2 Participation rate organised learning children SDG Regions (1VYPA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_PRE_PARTN.9+62+513+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/4_2_2_Participation_Rate_Learning_Children_SDG_Regions.csv', index=True)

#4.2.2 Participation rate organised learning children Nordics (gJTRQ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_PRE_PARTN.208+246+352+578+752._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_2_2_Participation_Rate_Learning_Children_Nordics.csv', index=True)

#4.3.1 Participation rate organised learning adults Nordics (3NoiA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_ADT_EDUCTRN.208+246+352+578+752._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_DETAIL', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.drop([2011, 2012], axis=0,inplace=True)
df_new.to_csv('data/4_3_1_Participation_Rate_Organised_Learning_Adults_Nordics.csv', index=True)

#4.4.1 ICT Skills Nordics (393Kw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_ADT_ACTS.208+246+352+578+752._T.......SKILL_ICTCPT+SKILL_ICTSSHT+SKILL_ICTPRGM+SKILL_ICTPST+SKILL_ICTSFWR+SKILL_ICTTRFF+SKILL_ICTCMFL.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
OECD = [74,73,12,54,70,60,63]
df_new['OECD'] = OECD
df_new.to_csv('data/4_4_1_ICT_Skills_Nordics.csv', index=True)

#4.7.1 Education Sustainable Development Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_GCEDESD_NEP+SE_GCEDESD_CUR+SE_GCEDESD_TED+SE_GCEDESD_SAS.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/4_7_1_Education_Sustainable_Development_Nordics.csv', index=True)

#4.a.1 Schools basic infrastructure World (uvdwQ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_ACS_ELECT+SE_ACS_CMPTR+SE_ACS_H2O+SE_ACC_HNDWSH+SE_ACS_INTNT+SE_ACS_SANIT+SE_INF_DSBL.1.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='EDUCATION_LEV', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/4_a_1_Schools_Basic_Infrastructure_World_Total.csv', index=True)

#4.c.1 Teachers qualifications World (uvdwQ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SE_TRA_GRDL.1+199._T....ISCED11_1+ISCED11_2+ISCED11_3....../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='EDUCATION_LEV', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 199: 'Least Developed Countries'}, inplace=True)
df_new.to_csv('data/4_c_1_Teachers_Qualifications_World_Total.csv', index=True)