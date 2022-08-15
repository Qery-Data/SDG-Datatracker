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