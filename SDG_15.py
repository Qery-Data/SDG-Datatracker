import requests
import os
import io
import pandas as pd
os.makedirs('data', exist_ok=True)
access_token = os.getenv('DW_TOKEN')

#15.1.1 Forest area as a share of total land area World and SDG regions (5qqbo)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRST.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Pct.change'] = (df_new.loc[2020] - df_new.loc[2000])/df_new.loc[2000]*100
df_new.to_csv('data/15_1_1_Forest_Area_Share_Total_Land_Area_World_SDG_Regions.csv', index=True)

#15.1.1 Forest area as a share of total land area Nordics (ZQzSJ)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRST.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_1_1_Forest_Area_Share_Total_Land_Area_Nordics.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas World (DZflH)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_FRHWTR+ER_PTD_TERR.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_World_Total.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas World and SDG regions (Pqi7o)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_FRHWTR+ER_PTD_TERR.53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_SDG_Regions.csv', index=True)

#15.1.2 Share of KBAs covered by protected areas Nordics (Msunw)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_TERR+ER_PTD_FRHWTR.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'ER_PTD_FRHWTR':'Freshwater KBAs', 'ER_PTD_TERR': 'Terrestial KBAs'}, inplace=True)
df_new.to_csv('data/15_1_2_Share_KBA_Covered_Protected_Areas_Nordics.csv', index=True)

#15.2.1 Forest area annual net change World and SDG regions (X6rvB)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTCHG.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/15_2_1_Forest_Area_Annual_Net_Change_World_SDG_Regions.csv', index=True)

#15.2.1 Above-ground biomass stock in forest World and SDG regions (eADyF)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTBIOPHA.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Above-ground_Biomass_Stock_Forest_World_SDG_Regions.csv', index=True)

#15.2.1 Proportion of forest area within legally established protected areas World and SDG regions (2B9ig)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTPRCT.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Share_Forest_Area_Within_Legally_Protected_Areas_World_SDG_Regions.csv', index=True)

#15.2.1 Proportion of forest area under a long-term management plan World and SDG regions (3h6OW)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTMGT.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Share_Forest_area_Under_Long-term_Management_Plan_World_SDG_Regions.csv', index=True)

#15.2.1 Forest area under an independently verified forest management certification scheme World and SDG regions (g01cP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTCERT.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.loc['Change 2021-2022'] = (df_new.loc[2022] - df_new.loc[2021])
df_new.to_csv('data/15_2_1_Forest_Area_Under_Independently_Verified_Forest_Management_Certification_Scheme_World_SDG_Regions.csv', index=True)

#15.2.1 Forest area annual net change Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTCHG.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_2_1_Forest_Area_Annual_Net_Change_Nordics.csv', index=True)

#15.2.1 Above-ground biomass stock in forest Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTBIOPHA.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Above-ground_Biomass_Stock_Forest_Nordics.csv', index=True)

#15.2.1 Proportion of forest area within legally established protected areas Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTPRCT.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Share_Forest_Area_Within_Legally_Protected_Areas_Nordics.csv', index=True)

#15.2.1 Proportion of forest area under a long-term management plan Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTMGT.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.loc['Pct_change 2010-2020'] = (df_new.loc[2020] - df_new.loc[2010])/df_new.loc[2010]*100
df_new.to_csv('data/15_2_1_Share_Forest_area_Under_Long-term_Management_Plan_Nordics.csv', index=True)

#15.2.1 Forest area under an independently verified forest management certification scheme Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..AG_LND_FRSTCERT.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.loc['Pct_change 2010-2022'] = (df_new.loc[2022] - df_new.loc[2021])/df_new.loc[2021]*100
df_new.to_csv('data/15_2_1_Forest_Area_Under_Independently_Verified_Forest_Management_Certification_Scheme_Nordics.csv', index=True)

#15.2.1 Intensity of use of forest resources (xxxxx)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/FOREST/INT_USE.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/15_2_1_Intensity_Forest_Resources_Nordics.csv', index=True)

#15.4.1 Share of mountain KBAs covered by protected areas World (yP08Z)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_MTN.1.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/15_4_1_Share_Mountain_KBA_Covered_Protected_Areas_World_Total.csv', index=True)

#15.4.1 Share of mountain KBAs covered by protected areas SDG regions (VjaRn)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_MTN.53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/15_4_1_Share_Mountain_KBA_Covered_Protected_Areas_SDG_Regions.csv', index=True)

#15.4.1 Share of mountain KBAs covered by protected areas Nordics (69hbU)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_PTD_MTN.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_4_1_Share_Mountain_KBA_Covered_Protected_Areas_Nordics.csv', index=True)

#15.5.1 Red List Index World (HdfLP)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_RSK_LST.1.........../ALL/?detail=full&startPeriod=1993-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/15_5_1_Red_List_Index_World_Total.csv', index=True)

#15.5.1 Red List Index SDG Regions (XpOMU)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_RSK_LST.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/15_5_1_Red_List_Index_World_Total_World_SDG_Regions.csv', index=True)

#15.5.1 Red List Index Nordics (jIwf7)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_RSK_LST.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_5_1_Red_List_Index_Nordics.csv', index=True)

#15.6.1 Adoption of legislative, administrative and policy frameworks World (Sh1My)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_CBD_ABSCLRHS+ER_CBD_NAGOYA+ER_CBD_PTYPGRFA+ER_CBD_ORSPGRFA.1.........../ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'ER_CBD_ABSCLRHS': 'Access and Benefit-Sharing Clearing-House', 'ER_CBD_NAGOYA': 'The Nagoya Protocol', 'ER_CBD_PTYPGRFA': 'The International Treaty on Plant Genetic Resources for Food and Agriculture', 'ER_CBD_ORSPGRFA':'Online Reporting System on Compliance of the International Treaty on Plant Genetic Resources for Food and Agriculture'},inplace=True)
df_new.to_csv('data/15_6_1_Adoption_Policy_Frameworks_World_Total.csv', index=True)

#15.6.1 Adoption of legislative, administrative and policy frameworks Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_CBD_ABSCLRHS+ER_CBD_NAGOYA+ER_CBD_PTYPGRFA+ER_CBD_ORSPGRFA.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'ER_CBD_ABSCLRHS': 'Access and Benefit-Sharing Clearing-House', 'ER_CBD_NAGOYA': 'The Nagoya Protocol', 'ER_CBD_PTYPGRFA': 'The International Treaty on Plant Genetic Resources for Food and Agriculture', 'ER_CBD_ORSPGRFA':'Online Reporting System on Compliance of the International Treaty on Plant Genetic Resources for Food and Agriculture'},inplace=True)
df_new.to_csv('data/15_6_1_Adoption_Policy_Frameworks_Nordics.csv', index=True)

#15.8.1 Measures to prevent IAS (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_IAS_LEGIS+ER_IAS_NBSAP+ER_IAS_NATBUD+ER_IAS_GLOFUN+ER_IAS_NBSAPP+ER_IAS_NATBUDP+ER_IAS_GLOFUNP.1.........../ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/15_8_1_Measures_IAS_World_Total.csv', index=True)

#15.8.1 Measures to prevent IAS Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_IAS_LEGIS+ER_IAS_NBSAP+ER_IAS_NATBUD+ER_IAS_GLOFUN+ER_IAS_NBSAPP+ER_IAS_NATBUDP+ER_IAS_GLOFUNP.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_8_1_Measures_IAS_Nordics.csv', index=True)

#15.9.1 Integrate ecosystem and biodiversity values nationally and locally World (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_BDY_ABT2NP+ER_BDY_SEEA.1........_T.../ALL/?detail=full&startPeriod=2015-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.to_csv('data/15_9_1_Integrate_Ecosystem_Biodiversity_Nationally_Locally_World_Total.csv', index=True)

#15.9.1 ABT2 Status World and SDG regions (T2ZL0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_BDY_ABT2NP.1+53+62+513+543+747+753+202+419........ABT2_ACHIEVE+ABT2_EXCEED+ABT2_INSUFNT+ABT2_DIGRESS+ABT2_NOPROG+ABT2_NONTLT.../ALL/?detail=full&startPeriod=2000-01-01&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.rename(index={'ABT2_ACHIEVE': 'National target reflecting ABT2 exists and progress is on track to achieve it', 'ABT2_DIGRESS': 'National target reflecting ABT2 exists, but moving away from it', 'ABT2_EXCEED': 'National target reflecting ABT2 exists and progress is on track to exceed it', 'ABT2_INSUFNT':'National target reflecting ABT2 exists and progress is there, but at as insufficient rate', 'ABT2_NONTLT': 'No national target reflecting ABT 2', 'ABT2_NOPROG': 'National target reflecting ABT2 exists, but no progress'},inplace=True)
df_new.to_csv('data/15_9_1_ABT2_Status_World_SDG_Regions.csv', index=True)

#15.9.1 Integrate ecosystem and biodiversity values nationally and locally Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_BDY_SEEA.208+246+352+578+752........_T.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_9_1_Integrate_Ecosystem_Biodiversity_Nationally_Locally_Nordics.csv', index=True)

#15.9.1 ABT2 Status Nordics (xxxxx)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..ER_BDY_ABT2NP.208+246+352+578+752........ABT2_ACHIEVE+ABT2_EXCEED+ABT2_INSUFNT+ABT2_DIGRESS+ABT2_NOPROG+ABT2_NONTLT.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/15_9_1_ABT2_Status_Nordics.csv', index=True)

#15.a.1 Total ODA to commitments on conservation and sustainable use of biodiversity and ecosystems World (vWrEH)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.14/..DC_ODA_BDVL.515.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={515:'Developing countries'}, inplace=True)
df_new.to_csv('data/15_a_1_ODA_Biodiversity_World_Total.csv', index=True)