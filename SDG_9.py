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

#9.2.1 Manufacturing value added as a proportion of GDP World (WXkql)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NV_IND_MANF.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_2_1_Manufacturing_Share_GDP_World_Total.csv', index=True)

#9.2.1 Manufacturing share of employment World (nZtTL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_MANF.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_2_2_Manufacturing_Share_Employment_World_Total.csv', index=True)

#9.2.1 Manufacturing value added per capita (nBsUE)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NV_IND_MANFPC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_2_2_Manufacturing_Value_Added_Per_Capita_World_Total.csv', index=True)

#9.2.1 Manufacturing value added as a proportion of GDP SDG Regions (nZ6FK)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NV_IND_MANF.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_2_1_Manufacturing_Share_GDP_SDG_Regions.csv', index=True)

#9.2.1 Manufacturing share of employment SDG Regions (hWg6f)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_TLF_MANF.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_2_2_Manufacturing_Share_Employment_SDG_Regions.csv', index=True)

#9.2.1 Manufacturing value added per capita SDG Regions (03Rtz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NV_IND_MANFPC.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_2_2_Manufacturing_Value_Added_Per_Capita_SDG_Regions.csv', index=True)

#9.2.1 Manufacturing value added per capita Nordics (rLnYU)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..NV_IND_MANFPC.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/9_2_2_Manufacturing_Value_Added_Per_Capita_Nordics.csv', index=True)

#9.3.1 Proportion of small-scale industries with a loan or line of credit World and SDG regions (0qMjA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FC_ACC_SSID.1+9+53+62+513+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1:'World', 9:'Oceania', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania','Australia and New Zealand','Latin America and the Caribbean'])
df_new.drop(['Australia and New Zealand'], axis=1, inplace=True)
df_new.to_csv('data/9_3_1_Share_Small_Scale_Industries_Credit_World_SDG_Regions.csv', index=True)

#9.4.1 CO2 emission per unit of manufacturing value added World (28cXS)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_ATM_CO2MVA.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_4_1_CO2_Emissions_Manufacturing_Value_Added_World_Total.csv', index=True)

#9.4.1 CO2 emission per GDP World (r7z45)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_ATM_CO2GDP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_4_1_CO2_Emissions_Per_GDP_World_Total.csv', index=True)

#9.4.1 CO2 emission per unit of manufacturing value added SDG Regions (voYOS)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_ATM_CO2MVA.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_4_1_CO2_Emissions_Manufacturing_Value_Added_SDG_Regions.csv', index=True)

#9.4.1 CO2 emission per unit of manufacturing value added Nordics (Ic2PJ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_ATM_CO2MVA.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/9_4_1_CO2_Emissions_Manufacturing_Value_Added_Nordics.csv', index=True)

#9.4.1 CO2 emission per GDP Nordics (rLnYU)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..EN_ATM_CO2GDP.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/9_4_1_CO2_Emissions_Per_GDP_Nordics.csv', index=True)

#9.5.1 R&D expenditure as share of GDP World (qfI48)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_XPD_RSDV.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_5_1_R&D_Share_GDP_World_Total.csv', index=True)

#9.5.1 R&D expenditure as share of GDP SDG Regions (aGop9)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_XPD_RSDV.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_5_1_R&D_Share_GDP_SDG_Regions.csv', index=True)

#9.5.1 R&D expenditure as share of GDP Nordics (YslB5)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_XPD_RSDV.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new = df_new.loc[[2015,2018]]
df_new.to_csv('data/9_5_1_R&D_Share_GDP_Nordics.csv', index=True)

#9.5.2 Researchers per million inhabitants World (gEWyM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_POP_SCIERD.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/9_5_2_Researcher_Density_World_Total.csv', index=True)

#9.5.2 Researchers per million inhabitants SDG Regions (X4doh)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_POP_SCIERD.53+62+513+543+747+753+202+419.........../?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/9_5_2_Researcher_Density_SDG_Regions.csv', index=True)

#9.5.2 Researchers per million inhabitants Nordics (ZMoqG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..GB_POP_SCIERD.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.drop(['Iceland'], axis=1, inplace=True)
df_new.to_csv('data/9_5_2_Researcher_Density_Nordics.csv', index=True)