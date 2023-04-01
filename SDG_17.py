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

#17.1.1 Total government revenue as a proportion of GDP World (0WlzW)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GR_G14_GDP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_1_1_Total_Government_Revenue_Share_GDP_World_Total.csv', index=True)

#17.1.1 Total government revenue as a proportion of SDG regions (8SHdD)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GR_G14_GDP.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_1_1_Total_Government_Revenue_Share_GDP_SDG_Regions.csv', index=True)

#17.1.1 Total government revenue as a proportion of GDP Nordics (2IKTg)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GR_G14_GDP.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_1_1_Total_Government_Revenue_Share_GDP_Nordics.csv', index=True)

#17.1.2 Proportion of domestic budget funded by domestic taxes World (XtTsV)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GC_GOB_TAXD.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_1_2_Share_Domestic_Budget_Funded_Domestic_Taxes_World_Total.csv', index=True)

#17.1.2 Proportion of domestic budget funded by domestic taxes SDG regions (Omsyv)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GC_GOB_TAXD.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_1_2_Share_Domestic_Budget_Funded_Domestic_Taxes_World_SDG_Regions.csv', index=True)

#17.1.2 Proportion of domestic budget funded by domestic taxes Nordics (2IKTg)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GC_GOB_TAXD.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_1_2_Share_Domestic_Budget_Funded_Domestic_Taxes_Nordics.csv', index=True)

#17.2.1 ODA as share of GNI DAC Total and Nordics (lLRPr/RaU35)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TABLE1/20001+3+18+20+8+10.1.11002.1160.A+D+N/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Donor', values='Value')
df_new.to_csv('data/17_2_1_DAC_ODA_GNI_Total_Nordics.csv', index=True)

#17.2.1 ODA as share of GNI to LDCs DAC Total and Nordics (4Mm89)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..DC_ODA_LDCG.208+246+352+578+593+752.........../ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway', 593: 'DAC-total', 752:'Sweden'},inplace=True)
df_new.to_csv('data/17_2_1_DAC_ODA_GNI_LDCs_Total_Nordics.csv', index=True)

#17.3.1 FDI inflows World (zpiNw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..GF_FRN_FDI.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_3_1_FDI_Inflows_World_Total.csv', index=True)

#17.3.2 Remittances as share of GDP World (AM1oG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..BX_TRF_PWKR.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_3_2_Remittances_Share_GDP_World_Total.csv', index=True)

#17.3.2 Remittances as share of GDP SDG regions (4bNgE)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..BX_TRF_PWKR.53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_3_2_Remittances_Share_GDP_SDG_Regions.csv', index=True)

#17.3.2 Remittances as share of GDP Nordics (3aCzK)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..BX_TRF_PWKR.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_3_2_Remittances_Share_GDP_Nordics.csv', index=True)

#17.4.1 Debt service as share of exports SDG regions (iI3iK)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..BX_TRF_PWKR.15+62+543+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={15:'Northern Africa', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_4_1_Debt_Service_Share_Exports_SDG_Regions.csv', index=True)

#17.5.1 Number of countries with a signed or an in force bilateral investment treaty (BIT) with developing countries World (KwAs3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_CPA_SIGN_BIT+SG_CPA_INFORCE_BIT.515.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'SG_CPA_INFORCE_BIT':'Inforce', 'SG_CPA_SIGN_BIT': 'Signed'}, inplace=True)
df_new.to_csv('data/17_5_1_Signed_Inforce_BIT_Developing_Countries_World_Total.csv', index=True)

#17.5.1 Number of countries with a signed or an in force bilateral investment treaty (BIT) with LDCs World (Nvdqz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_CPA_SIGN_BIT+SG_CPA_INFORCE_BIT.199.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'SG_CPA_INFORCE_BIT':'Inforce', 'SG_CPA_SIGN_BIT': 'Signed'}, inplace=True)
df_new.to_csv('data/17_5_1_Signed_Inforce_BIT_LDCS_World_Total.csv', index=True)

#17.7.1 Amount of tracked exported Environmentally Sound Technologies World (rdDbM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..DC_ENVTECH_EXP+DC_ENVTECH_IMP.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.loc['Total'] = (df_new.loc['DC_ENVTECH_EXP'] + df_new.loc['DC_ENVTECH_IMP'])
df_new.to_csv('data/17_7_1_Amount_Tracked_Exported_Environmentally_Sound_Technologies_World_Total.csv', index=True)

#17.8.1 Share of individuals using the internet World (8DnzP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..IT_USE_II99.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_8_1_Share_Individuals_Using_Internet_World_Total.csv', index=True)

#17.8.1 Share of individuals using the internet World SDG regions (b1YWK)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..IT_USE_II99.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_8_1_Share_Individuals_Using_Internet_World_SDG_Regions.csv', index=True)

#17.8.1 Share of individuals using the internet last 3m Nordics (192Eu)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/ICT_HH2/DNK+FIN+ISL+NOR+SWE.C5B.IND_TOTAL/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Time', columns='Country', values='Value')
df_new.to_csv('data/17_8_1_Share_Individuals_Using_Internet_last3M_Nordics.csv', index=True)

#17.9.1 Total ODA for technical cooperation World (yn4HM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..DC_FTA_TOTAL.515.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={511:'Developing countries'}, inplace=True)
df_new.to_csv('data/17_9_1_Total_ODA_Technical_Cooperation_World_Total.csv', index=True)

#17.10.1 Worldwide weighted tariff-average of all products World (yn4HM)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_WMFN+TM_TAX_WMPS.1..........._T/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'TM_TAX_WMFN':'Most-favoured-nation status', 'TM_TAX_WMPS':'Preferential status'}, inplace=True)
df_new.to_csv('data/17_10_1_Worldwide_Weighted_Tariff_Average_All_Products_World_Total.csv', index=True)

#17.10.1 Worldwide weighted tariff-average of by product World (wVjSm)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_WMPS.1...........AGG_ARMS+AGG_CLTH+AGG_IND+AGG_AGR+AGG_OIL+AGG_TXT/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='PRODUCT', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'AGG_AGR':'Agricultural products', 'AGG_ARMS':'Arms', 'AGG_CLTH': 'Clothing', 'AGG_IND':'Industrial Products', 'AGG_OIL':'Oil', 'AGG_TXT':'Textiles'}, inplace=True)
df_new.to_csv('data/17_10_1_Worldwide_Weighted_Tariff_Average_By_Product_World_Total.csv', index=True)

#17.10.1 Worldwide weighted tariff-average of all products SDG regions (p7gpb)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_WMPS.1+53+62+513+543+747+753+202+419..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/17_10_1_Worldwide_Weighted_Tariff_Average_All_Products_World_SDG_Regions.csv', index=True)

#17.10.1 Weighted tariff-average of all products Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_WMPS.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_10_1_Weighted_Tariff_Average_All_Products_Nordics.csv', index=True)

#17.11.1 Developing countries share of global exports (ejH3U)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TX_EXP_GBMRCH+TX_EXP_GBSVR.515.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'TX_EXP_GBMRCH':'Global merchandise exports', 'TX_EXP_GBSVR':'Global service exports'}, inplace=True)
df_new.to_csv('data/17_11_1_Developing_Countries_Share_Exports.csv', index=True)

#17.11.1 LDCs share of global exports (bV0AG)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TX_EXP_GBMRCH+TX_EXP_GBSVR.199.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'TX_EXP_GBMRCH':'Global merchandise exports', 'TX_EXP_GBSVR':'Global service exports'}, inplace=True)
df_new.to_csv('data/17_11_1_LDCs_Share_Exports.csv', index=True)

#17.12.1 Average tariff applied by developed countries on key products (l2vIc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_DPRF.199+515+722..........._T/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={199:'Least developed countries', 515:'Developing countries', 722: 'Small-island developing States'}, inplace=True)
df_new.to_csv('data/17_12_1_Average_Tariff_Developed_Countries.csv', index=True)

#17.12.1 Average tariff applied preferential status Nordics (5Suqx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_DPRF.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_12_1_Average_Tariff_Applied_Preferential_Nordics.csv', index=True)

#17.12.1 Average tariff applied MFN by Nordics (5LClA)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..TM_TAX_DMFN.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_12_1_Average_Tariff_Applied_MFN_Nordics.csv', index=True)

#17.13.1 Macroeconomic Dashboard Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..FB_BNK_CAPA_ZS+FM_LBL_BMNY_ZG+FM_LBL_BMNY_IR_ZS+BN_CAB_XOKA_GD_ZS+NE_EXP_GNFS_KD_ZG+DT_DOD_DECT_GN_ZS+BX_KLT_DINV_WD_GD_ZS+NY_GDP_MKTP_KD_ZG+NE_CON_GOVT_KD_ZG+NE_GDI_TOTL_KD_ZG+NE_IMP_GNFS_KD_ZG+FP_CPI_TOTL_ZG+TG_VAL_TOTL_GD_ZS+BN_KLT_PTXL_CD+GC_TAX_TOTL_GD_ZS+FI_RES_TOTL_MO+DP_DOD_DLD2_CR_CG_Z1+GC_BAL_CASH_GD_ZS+PA_NUS_ATLS+NE_CON_PRVT_KD_ZG.208+246+352+578+752..........._T/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_13_1_Macroeconomic_Dashboard_Nordics.csv', index=True)

#17.15.1 Extent of use of country-owned results frameworks and planning tools by providers of development cooperation World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_PLN_PRPOLRES.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_15_1_Extent_Country_Owned_Results_World_Total.csv', index=True)

#17.15.1 Extent of use of country-owned results frameworks and planning tools by providers of development cooperation Nordics (Qn3Lc)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_PLN_PRPOLRES.1+208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World average', 208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_15_1_Extent_Country_Owned_Results_Nordics.csv', index=True)

#17.16.1 Number of countries reporting progress in multi-stakeholder development effectiveness monitoring frameworks that support the SDGs World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_PLN_MSTKSDG_P+SG_PLN_MSTKSDG_R.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'SG_PLN_MSTKSDG_P':'Provider', 'SG_PLN_MSTKSDG_R': 'Recipient'}, inplace=True)
df_new.to_csv('data/17_16_1_Number_Countries_Multistakeholder_Development_Effectiveness_Monitoring_Frameworks_World_Total.csv', index=True)

#17.16.1 Multi-stakeholder development effectiveness monitoring frameworks that support the SDGs Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_PLN_MSTKSDG_P.208+246+352+578+752..........._T/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_16_1_Multistakeholder_Development_Effectiveness_Monitoring_Frameworks_Nordics.csv', index=True)

#17.18.2 Number of countries that have national statistical legislation that complies with the Fundamental Principles of Official Statistics World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_STT_FPOS.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_18_2_Number_Countries_National_Statistics_Legislation_Complies_FundPrinc_World_Total.csv', index=True)

#17.18.3 Number of countries that national statistics plans under implementation and fully funded World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_STT_NSDSFND+SG_STT_NSDSIMPL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'SG_STT_NSDSFND':'Fully funded', 'SG_STT_NSDSIMPL': 'Under implementation'}, inplace=True)
df_new.to_csv('data/17_18_3_Number_Countries_Statistics_Plans_Implementation_Fully_Funded_World_Total.csv', index=True)

#17.18.3 Countries that national statistics plans under implementation and fully funded Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_STT_NSDSFND+SG_STT_NSDSIMPL.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/17_18_3_Statistics_Plans_Implementation_Fully_Funded_Nordics.csv', index=True)

#17.19.1 Dollar value of all resources made available to strengthen statistical capacity World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_STT_CAPTY.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/17_19_1_Dollar_Value_Resources_Strenghten_Statistical_Capacity_World_Total.csv', index=True)

#17.19.2 Share of countries a)conducted at least one population and housing census in the last 10 years; and (b) have achieved 100 per cent birth registration and 80 per cent death registration World (xxxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SG_REG_BRTH90+SG_REG_CENSUS+SG_REG_DETH75.1+53+62+513+543+747+753+202+419..........._T/ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'SG_REG_BRTH90':'Birth registration data at least 90 pct complete', 'SG_REG_DETH75': 'Death registration data at least 75 pct complete', 'SG_REG_CENSUS': 'Conducted at least one population and housing census in the last 10 years'}, inplace=True)
df_new.to_csv('data/17_19_2_Share_Countries_Census_Birth_Death_World_SDG_Regions.csv', index=True)