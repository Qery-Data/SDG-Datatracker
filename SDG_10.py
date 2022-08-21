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

#10.2.1 Proportion of people below 50% median income Nordics (Pfv60)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SI_POV_50MI.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/10_2_1_Proportion_below_50pct_Median_Income_Nordics.csv', index=True)

#10.4.1 Labour share of GDP World (ZYOdO)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_GTOTL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/10_4_1_Labour_Share_World_Total.csv', index=True)

#10.4.1 Labour share of GDP SDG Regions (7N3Zp)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SL_EMP_GTOTL.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Oceania*','Australia and New Zealand','Latin America and the Caribbean'])
df_new.to_csv('data/10_4_1_Labour_Share_SDG_Regions.csv', index=True)

#10.5.1 Financial soundness indicators Nordics (91XhC)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..FI_FSI_FSANL+FI_FSI_FSERA+FI_FSI_FSKA+FI_FSI_FSKNL+FI_FSI_FSKRTC+FI_FSI_FSLS+FI_FSI_FSSNO.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2020-01-01&endPeriod=2020-12-31&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.insert(4,"OECD 2030-target", [1, 2, 12, 2,22, 130,-24], True)
df_new.rename(index={'FI_FSI_FSANL':'Non-performing loans to total gross loans (%)', 'FI_FSI_FSERA':'Return on assets  (%)', 'FI_FSI_FSKA': 'Regulatory capital to assets (%)', 'FI_FSI_FSKNL':'Non-performing loans net of provisions to capital (%)', 'FI_FSI_FSKRTC': 'Regulatory Tier 1 capital to risk-weighted assets (%)', 'FI_FSI_FSLS': 'Liquid assets to short term liabilities (%)', 'FI_FSI_FSSNO': 'Net open position in foreign exchange to capital (%)'}, inplace=True)
df_new.to_csv('data/10_5_1_Financial_Soundness_Indicators_Nordics.csv', index=True)

#10.6.1 Membership and Voting rights Developing regions (mAJEt)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SG_INT_MBRDEV+SG_INT_VRTDEV.515.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={'IO_ADB':'Asian Development Bank','IO_AFDB':'African Development Bank', 'IO_ECOSOC':'UN Economic and Social Council', 'IO_FSB': 'Financial Stability Board', 'IO_IADB':'Inter-American Development Bank', 'IO_IBRD':'International Bank for Reconstruction and Development', 'IO_IFC':'International Finance Corporation', 'IO_IMF': 'International Monetary Fund', 'IO_UNGA':'UN General Assembly', 'IO_UNSC':'UN Security Council','IO_WTO':'World Trade Organisation'}, inplace=True)
df_new.rename(columns={'SG_INT_MBRDEV':'Share of members', 'SG_INT_VRTDEV':'Share of voting rights'},inplace=True)
df_new.to_csv('data/10_6_1_Membership_Voting_Rights_Developing_Regions.csv', index=True)

#10.7.2 Migration policies that meet criteria World and SDG Regions (HWUCM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SG_CPA_MIGRP.1+53+62+513+543+747+753+202+419........_T.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/10_7_2_Migration_Policies_Share_World_SDG_Regions.csv', index=True)

#10.7.2 Migration policies that meet criteria Nordics (huLWV)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SG_CPA_MIGRS.208+246+352+578+752........_T+PD_1+PD_2+PD_3+PD_4+PD_5+PD_6.../ALL/?detail=full&startPeriod=2020-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'_T':'Overall', 'PD_1':'Migrant rights', 'PD_2': 'Whole-of-government/ Evidence-based policies', 'PD_3':'Cooperation and partnerships', 'PD_4': 'Socioeconomic well-being', 'PD_5': 'Mobility dimensions of crises', 'PD_6': 'Safe, orderly and regular migration'}, inplace=True)
df_new.to_csv('data/10_7_2_Migration_Policies_Nordics.csv', index=True)

#10.7.3 Migrant deaths World (oEIDN)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SM_DTH_MIGR.1.........../ALL/?detail=full&startPeriod=2000-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/10_7_3_Migrants_Deaths_World_Total.csv', index=True)

#10.7.3 Proportion of population refugees World (Ur0LL)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SM_POP_REFG_OR.1.........../ALL/?detail=full&startPeriod=2000-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/10_7_4_Proportion_Population_Refugees_World_Total.csv', index=True)

#10.a.1 Share of tariff lines with zero-tariffs LDCs + Dev.reg (2mO6y)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..TM_TRF_ZERO.199+515..........._T/ALL/?detail=full&startPeriod=2000-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={199:'Least Developed Countries',515:'Developing regions'}, inplace=True)
df_new.to_csv('data/10_a_1_Share_Zero_Tariffs_DevandLDCs.csv', index=True)

#10.a.1 Share of tariff lines with zero-tariffs by product LDCs + Dev.reg (U5HVV)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..TM_TRF_ZERO.199+515...........AGG_ARMS+AGG_CLTH+AGG_IND+AGG_AGR+AGG_OIL+AGG_TXT/ALL/?detail=full&lastnObservations=1&&format=csv')
df_new = df_csv.pivot(index='PRODUCT', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={199:'Least Developed Countries',515:'Developing regions'}, inplace=True)
df_new.rename(index={'AGG_AGR':'Agricultural products', 'AGG_ARMS':'Arms','AGG_CLTH':'Clothing','AGG_IND':'Industrial products', 'AGG_OIL':'Oil','AGG_TXT':'Textiles'}, inplace=True)
df_new.to_csv('data/10_a_1_Share_Zero_Tariffs_Product_DevandLDCs.csv', index=True)

#10.a.1 Share of tariff lines with zero-tariffs Nordics (FKARc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..TM_TRF_ZERO.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/10_a_1_Share_Zero_Tariffs_Nordics.csv', index=True)

#10.b.1 Total financial flows (hDIUH)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..DC_TRF_TFDV.515.........../ALL/?detail=full&startPeriod=2000-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={515:'Developing regions'}, inplace=True)
df_new.to_csv('data/10_b_1_Total_Financial_Flows_Total.csv', index=True)

#10.c.1 Remittance costs World (qtO64)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.9/..SI_RMT_COST.1.........../ALL/?detail=full&startPeriod=2000-01-01&endPeriod=2021-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/10_c_1_Remittance_Costs_World_Total.csv', index=True)