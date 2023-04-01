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

#16.1.1 Victims of homicides World (fjzyh)
#df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_IHR_PSRC.1._T.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
#df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
#df_new.rename(index={1:'World'}, inplace=True)
#df_new.to_csv('data/16_1_1_Victims_Homicides_World_Total.csv', index=True)

#16.1.1 Victims of homicides World and SDG regions (DMebq)
#df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_IHR_PSRC.1+53+62+513+543+747+753+202+419._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
#df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
#df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
#df_new.to_csv('data/16_1_1_Victims_Homicides_World_SDG_Regions.csv', index=True)

#16.1.1 Victims of homicides Nordics (TOMaQ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_IHR_PSRC.208+246+352+578+752._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_1_1_Victims_Homicides_Nordics.csv', index=True)

#16.1.2 Conflict related deaths World (dc8xw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_DTH_TOTR.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_1_2_Conflict_Related_Deaths_World_Total.csv', index=True)

#16.1.4 Share of population who feel safe walking alone around the area they live after dark World and SDG Region (JxjFP)
#df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_SNS_WALN_DRK.1+53+62+513+543+747+753+202+419._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
#df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
#df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
#df_new.to_csv('data/16_1_4_Share_Safe_After_Dark_World_SDG_Regions.csv', index=True)

#16.1.4 Share of population who feel safe walking alone around the area they live after dark Nordics (X6ekj)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_SNS_WALN_DRK.208+246+352+578+752._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_1_4_Share_Safe_After_Dark_Nordics.csv', index=True)

#16.2.1 Share of children from 1 to 14 years of age were subjected to some form of psychological aggression and/or physical punishment at home in the past month World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_PHYPYV.1._T.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_2_1_Share_Children_Psychological_Agression_Physical_Punishment_World_Total.csv', index=True)

#16.2.2 Number of victims of human trafficking Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_HTF_DETV.208+246+352+578+752._T._T........./ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_2_2_Number_Victims_Human_Trafficing_Nordics.csv', index=True)

#16.2.3 Share of women aged 18‑29 years who experienced sexual violence by age 18 World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_SXVLN.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_2_3_Share_Women_Experience_Sexual_Violence_World_Total.csv', index=True)

#16.2.3 Share of women aged 18‑29 years who experienced sexual violence by age 18 Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_SXVLN.208+246+352+578+752.F.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_2_3_Share_Women_Experience_Sexual_Violence_Nordics.csv', index=True)

#16.2.3 Share of men aged 18‑29 years who experienced sexual violence by age 18 Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_SXVLN.208+246+352+578+752.M.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_2_3_Share_Men_Experience_Sexual_Violence_Nordics.csv', index=True)

#16.3.2 Unsentenced detainees as a proportion of overall prison population World (xxxxx)
#df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_PRS_UNSNT.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
#df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
#df_new.rename(index={1:'World'}, inplace=True)
#df_new.to_csv('data/16_3_2_Unsentenced_Detainees_Share_Overall_Prison_Population_World_Total.csv', index=True)

#16.3.2 Unsentenced detainees as a proportion of overall prison population World and SDG regions (0dDfx)
#df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_PRS_UNSNT.1+53+62+513+543+747+753+202+419._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
#df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
#df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
#df_new.to_csv('data/16_3_2_Unsentenced_Detainees_Share_Overall_Prison_Population_World_SDG_Regions.csv', index=True)

#16.3.2 Unsentenced detainees as a proportion of overall prison population Nordics (9Yawg)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_PRS_UNSNT.208+246+352+578+752._T.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_3_2_Unsentenced_Detainees_Share_Overall_Prison_Population_Nordics.csv', index=True)

#16.5.2 Bribery incidence in business World and SDG regions (wcOif)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..IC_FRM_BRIB.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_5_2_Bribery_Incidence_World_SDG_Regions.csv', index=True)

#16.5.2 Bribery incidence in business Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..IC_FRM_BRIB.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_5_2_Bribery_Incidence_Nordics.csv', index=True)

#16.6.2 Citizens confidence in the judicial system Nordics (p0Uzo)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/GOV/DNK+FIN+ISL+NOR+SWE+OAVG.CONF_JS/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/16_6_2_Citizens_Confidence_Judicial_System_Nordics.csv', index=True)

#16.7.1  Ratio for female and youth members of parliaments World and SDG regions (MXGeP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DMK_PARLMP_UC+SG_DMK_PARLMP_LC+SG_DMK_PARLYR_LC+SG_DMK_PARLYR_UC.1+53+62+513+543+747+753+202+419............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'SG_DMK_PARLMP_LC': 'Female, lower', 'SG_DMK_PARLMP_UC': 'Female, upper','SG_DMK_PARLYR_LC':'Youth, lower','SG_DMK_PARLYR_UC': 'Youth, upper'}, inplace=True)
df_new.to_csv('data/16_7_1_Ratio_Female_Youth_Members_Parliaments_World_SDG_Regions.csv', index=True)

#16.7.1  Number of speakers by sex in upper chambers World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DMK_PARLSP_UC.1+53+62+513+543+747+753+202+419.F+M........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SEX', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_7_1_Number_Speakers_Upper_Chambers_World_SDG_Regions.csv', index=True)

#16.7.1  Number of speakers by sex in lower chambers World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DMK_PARLSP_LC.1+53+62+513+543+747+753+202+419.F+M........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SEX', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_7_1_Number_Speakers_Lower_Chambers_World_SDG_Regions.csv', index=True)

#16.7.1  Ratio for female and youth members of parliaments Nordics (oaR5C)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_DMK_PARLMP_UC+SG_DMK_PARLMP_LC+SG_DMK_PARLYR_LC+SG_DMK_PARLYR_UC.208+246+352+578+752............/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SG_DMK_PARLMP_LC': 'Female', 'SG_DMK_PARLMP_UC': 'Female, upper','SG_DMK_PARLYR_LC':'Youth','SG_DMK_PARLYR_UC': 'Youth, upper'}, inplace=True)
df_new.to_csv('data/16_7_1_Ratio_Female_Youth_Members_Parliaments_Nordics.csv', index=True)

#16.9.1 Share of children under 5 years of age whose births have been registered World and SDG Regions (KdER0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_REG_BRTH.1+53+62+513+543+747+753+202+419..Y0T4........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_9_1_Share_Children_Under5_Births_Registered_World_SDG_Regions.csv', index=True)

#16.9.1 Share of children under 5 years of age whose births have been registered Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_REG_BRTH.208+246+352+578+752............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_9_1_Share_Children_Under5_Births_Registered_Nordics.csv', index=True)

#16.10.1 Number of cases of killings of human rights defenders, journalists and trade unionists World (XPY6m)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_MTUHRA.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_10_1_Number_Killings_HumRigJournTradeUni_World_Total.csv', index=True)

#16.10.1 Number of cases of killings of human rights defenders, journalists and trade unionists SDG Regions (Vxipg)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VAW_MTUHRA.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_10_1_Number_Killings_HumRigJournTradeUni_SDG_Regions.csv', index=True)

#16.10.1 Number of enforced disapperances of human rights defenders, journalists and trade unionists World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..VC_VOC_ENFDIS.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_10_1_Number_Enforced_Disapperances_HumRigJournTradeUni_World_Total.csv', index=True)

#16.10.2 Number of countries that adopt and implement constitutional, statutory and/or policy guarantees for public access to information World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_INF_ACCSS.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_10_2_Number_Countries_Adopt_Implement_Guarantees_World_Total.csv', index=True)

#16.a.1 Share of countries with independent National Human Rights Institutions in compliance with the Paris Principles World and SDG Regions (wmAX7)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_NHR_IMPL.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/16_a_1_Share_Countries_Compliance_Paris_Principles_World_SDG_Regions.csv', index=True)

#16.a.1 Share of countries with independent National Human Rights Institutions in compliance with the Paris Principles World (TILId)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_NHR_IMPL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/16_a_1_Share_Countries_Compliance_Paris_Principles_World_Total.csv', index=True)

#16.a.1 Compliance with the Paris Principles Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_NHR_IMPLN+SG_NHR_INTEXSTN+SG_NHR_NOAPPLN+SG_NHR_NOSTUSN.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/16_a_1_Compliance_Paris_Principles_Nordics.csv', index=True)