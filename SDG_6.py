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

#6.1.1 Safe and affordable water World (Jbv5s)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_H2O_SAFE.1..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_1_1_Safe_Affordable_Water_World_Total.csv', index=True)

#6.1.1 Safe and affordable water SDG Regions (m2JAj)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_H2O_SAFE.9+62+513+747+753+202+419..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_1_1_Safe_Affordable_Water_SDG_Regions.csv', index=True)

#6.1.1 Safe and affordable water Nordics (jgvJn)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_H2O_SAFE.208+246+352+578+752..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_1_1_Safe_Affordable_Water_Nordics.csv', index=True)

#6.2.1a Safely managed sanitation World (TCMAc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_SAFE.1..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_2_1a_Safely_Managed_Sanitation_World_Total.csv', index=True)

#6.2.1a Safely managed sanitation SDG Regions (SWbYY)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_SAFE.9+62+513+747+753+202+419..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_2_1a_Safely_Managed_Sanitation_SDG_Regions.csv', index=True)

#6.2.1a Safely managed sanitation Nordics (KByGf)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_SAFE.208+246+352+578+752..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_2_1a_Safely_Managed_Sanitation_Nordics.csv', index=True)

#6.2.1b Basic handwashing facilities World (qqltF)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_HNDWSH.1..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_2_1b_Basic_Handwashing_Facilities_World_Total.csv', index=True)

#6.2.1b Basic handwashing facilities SDG Regions (VDF3y)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_HNDWSH.9+62+513+747+753+202+419..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_2_1b_Basic_Handwashing_Facilities_SDG_Regions.csv', index=True)

#6.2.1c Practicing open defecation World (l9f22)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_DEFECT.1..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_2_1c_Practicing_Open_Defecation_World_Total.csv', index=True)

#6.2.1c Practicing open defecation SDG Regions (jcjlk)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_SAN_DEFECT.9+62+513+747+753+202+419..._T......../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_2_1c_Practicing_Open_Defecation_SDG_Regions.csv', index=True)

#6.3.1 Domestic wastewater safely treated World and SDG Regions (K4mhg)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..EN_WWT_WWDS.1+9+62+513+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_3_1_Domsetic_Wastewater_World_SDG_Regions.csv', index=True)

#6.3.1 Domestic wastewater safely treated Nordics (kF8ZA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..EN_WWT_WWDS.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_3_1_Domsetic_Wastewater_Nordics.csv', index=True)

#6.3.2 Bodies of water with good ambient water quality World and SDG regions (hxnzG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_H2O_OPAMBQ+EN_H2O_RVAMBQ+EN_H2O_GRAMBQ+EN_H2O_WBAMBQ.1+9+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.rename(index={'EN_H2O_GRAMBQ': 'Proportion of groundwater bodies with good ambient water quality', 'EN_H2O_OPAMBQ': 'Proportion of open water bodies with good ambient water quality', 'EN_H2O_RVAMBQ': 'Proportion of river water bodies with good ambient water quality', 'EN_H2O_WBAMBQ': 'Proportion of bodies of water with good ambient water quality'},inplace=True)
df_new.to_csv('data/6_3_2_Bodies_Water_Good_Ambient_Quality_World_SDG_Regions.csv', index=True)

#6.3.2 Bodies of water with good ambient water quality Nordics (CYwuV)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_H2O_OPAMBQ+EN_H2O_RVAMBQ+EN_H2O_GRAMBQ+EN_H2O_WBAMBQ.208+246+352+578+752..._T......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'EN_H2O_GRAMBQ': 'Proportion of groundwater bodies with good ambient water quality', 'EN_H2O_OPAMBQ': 'Proportion of open water bodies with good ambient water quality', 'EN_H2O_RVAMBQ': 'Proportion of river water bodies with good ambient water quality', 'EN_H2O_WBAMBQ': 'Proportion of bodies of water with good ambient water quality'},inplace=True)
df_new.to_csv('data/6_3_2_Bodies_Water_Good_Ambient_Quality_Nordics.csv', index=True)

#6.4.1 Water-use efficiency World (M3KZi)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_WUEYST.1.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_4_1_Water_Use_Efficiency_World_Total.csv', index=True)

#6.4.1 Water-use efficiency SDG regions (ssMuD)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_WUEYST.9+62+513+747+753+202+419.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_4_1_Water_Use_Efficiency_SDG_Regions.csv', index=True)

#6.4.1 Water-use efficiency Nordics (Y0tFm)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_WUEYST.208+246+352+578+752.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_4_1_Water_Use_Efficiency_Nordics.csv', index=True)

#6.4.2 Level of water stress World (RhJxE)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_STRESS.1.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/6_4_2_Level_Water_Stress_World_Total.csv', index=True)

#6.4.2 Level of water stress SDG regions (lSQ0L)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_STRESS.9+62+513+747+753+202+419.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Latin America and the Caribbean'])
df_new.to_csv('data/6_4_2_Level_Water_Stress_SDG_Regions.csv', index=True)

#6.4.2 Level of water stress Nordics (EGlJM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_STRESS.208+246+352+578+752.........._T./ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_4_2_Level_Water_Stress_Nordics.csv', index=True)

#6.5.1 Degree of IWRM World and SDG regions (wcxwM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_IWRMD.1+9+62+513+747+753+202+419.........../ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 9: 'Oceania', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/6_5_1_Degree_IWRM_World_SDG_Regions.csv', index=True)

#6.5.1 Degree of IWRM Nordics (L5LLR)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_IWRMD.208+246+352+578+752.........._T./ALL/?detail=full&startPeriod=2017-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/6_5_1_Degree_IWRM_Nordics.csv', index=True)

#6.5.2 Transboundary basins with an operational arrangement for water cooperation (ZNJ3q)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_TBA_H2CO+EG_TBA_H2COAQ+EG_TBA_H2CORL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(columns={1:'World'}, inplace=True)
df_new.rename(index={'EG_TBA_H2CO':'River and lake basins, and aquifers','EG_TBA_H2CORL':'River and lake basins component','EG_TBA_H2COAQ':'Aquifers component'}, inplace=True)
df_new.to_csv('data/6_5_2_Transboundary_Basins_World_Total.csv', index=True)

#6.5.2 Transboundary basins with an operational arrangement for water cooperation Nordics (XBnXL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EG_TBA_H2CO+EG_TBA_H2COAQ+EG_TBA_H2CORL.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'EG_TBA_H2CO':'River and lake basins, and aquifers','EG_TBA_H2CORL':'River and lake basins component','EG_TBA_H2COAQ':'Aquifers component'}, inplace=True)
df_new.to_csv('data/6_5_2_Transboundary_Basins_Nordics_Total.csv', index=True)

#6.a.1 ODA for water supply and sanitation (rOSqC)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..DC_TOF_WASHL.515.........../ALL/?detail=full&startPeriod=2005-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(columns={515:'Total'}, inplace=True)
df_new.to_csv('data/6_a_1_ODA_Water_Sanitation_World_Total.csv', index=True)

#6.b.1 Local engagement procedures World (M6koE)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_WAT_PROCED+ER_H2O_PROCED.1..._T+R......../ALL/?detail=full&lastNObservations=1&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='SERIES', values='OBS_VALUE')
df_new.rename(columns={'ER_H2O_PROCED':'Rural drinking- water supply','ER_WAT_PROCED': 'Water resources planning and management'},inplace=True)
df_new.to_csv('data/6_b_1_Local_Engagement_Procedures_World.csv', index=True)

#6.b.1 Local engagement participation World (EYJin)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..ER_H2O_PARTIC+ER_WAT_PARTIC.1..._T+R......../ALL/?detail=full&lastNObservations=1&format=csv')
df_new= df_csv.pivot(index='TIME_PERIOD', columns='SERIES', values='OBS_VALUE')
df_new.rename(columns={'ER_H2O_PARTIC':'Rural drinking- water supply','ER_WAT_PARTIC':'Water resources planning and management'},inplace=True)
df_new.to_csv('data/6_b_1_Local_Engagement_Participation_World.csv', index=True)


