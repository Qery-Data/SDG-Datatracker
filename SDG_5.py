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

#5.1.1 Legal frameworks World and SDG Regions (a0XKn)
#Area 1 overarching legal frameworks and public life
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQLFP.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_1 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_1.rename(index={2020: 'Area 1: Overarching legal frameworks and public life'},inplace=True)
#Area 2 violence against women
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQVAW.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_2 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_2.rename(index={2020: 'Area 2:  Violence against women'},inplace=True)
#Area 3 employment and economic benefits
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQEMP.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_3 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_3.rename(index={2020: 'Area 3: Employment and economic benefits'},inplace=True)
#Area 4 marriage and family
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQMAR.1+53+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new_area_4 = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Latin America and the Caribbean'])
df_new_area_4.rename(index={2020: 'Area 4: Marriage and family'}, inplace=True)
df_all = pd.concat([df_new_area_1,df_new_area_2,df_new_area_3,df_new_area_4], axis=0)
df_all.loc['Average across all areas'] = df_all.mean(axis=0)
df_all.to_csv('data/5_1_1_Legal_Frameworks_World_SDG_Regions.csv', index=True)

#5.1.1 Legal frameworks Nordics (G8kF0)
#Area 1 overarching legal frameworks and public life
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQLFP.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_1 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_1.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_1.rename(index={2020: 'Area 1: Overarching legal frameworks and public life'},inplace=True)
#Area 2 violence against women
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQVAW.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_2 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_2.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_2.rename(index={2020: 'Area 2:  Violence against women'},inplace=True)
#Area 3 employment and economic benefits
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQEMP.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_3 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_3.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_3.rename(index={2020: 'Area 3: Employment and economic benefits'},inplace=True)
#Area 4 marriage and family
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_LGL_GENEQMAR.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_area_4 = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new_area_4.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new_area_4.rename(index={2020: 'Area 4: Marriage and family'}, inplace=True)
df_all = pd.concat([df_new_area_1,df_new_area_2,df_new_area_3,df_new_area_4], axis=0)
df_all.loc['Average across all areas'] = df_all.mean(axis=0)
df_all.to_csv('data/5_1_1_Legal_Frameworks_Nordics.csv', index=True)

#5.2.1 Violence women World and SDG regions (L0gR0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..VC_VAW_MARR.1+150+15+21+53+30+34+35+143+145+202+419+543..Y_GE15........./ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 150:'Europe', 15:'Northern Africa', 21:'Northern America', 53:'Australia and New Zeland',30:'Eastern Asia',34:'Southern Asia',35:'South-Eastern Asia', 143:'Central Asia', 145:'Western Asia',202:'Sub-Saharan Africa', 419:'Latin America and the Caribbean', 543:'Oceania*'},inplace=True)
df_new.to_csv('data/5_2_1_Violence_Women_World_SDG_Regions.csv', index=True)

#5.2.1 Violence women Nordics (bKbpd)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..VC_VAW_MARR.208+246+352+578+752..Y_GE15........./ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/5_2_1_Violence_Women_Nordics.csv', index=True)

#5.3.1 Women married union before age 15 18 World (NFYU3)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF15.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new_15 = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new_15.rename(index={1:'Before 15'}, inplace=True)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF18.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new_18 = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new_18.rename(index={1:'Before 18'}, inplace=True)
df_all = pd.concat([df_new_15,df_new_18], axis=0)
df_all.to_csv('data/5_3_1_Women_Married_Union_15_18_World_Total.csv', index=True)

#5.3.1 Women married union before age 15 and 18 SDG Regions (wBfDz)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF15.35+53+62+145+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_15 = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new_15.rename(columns={'SP_DYN_MRBF15':'Before age 15'},inplace=True)
df_new_15.rename(index={35: 'South-Eastern Asia', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 145: 'Western Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)

df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SP_DYN_MRBF18.35+53+62+145+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new_18 = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new_18.rename(columns={'SP_DYN_MRBF18':'Before age 18'},inplace=True)
df_new_18.rename(index={35: 'South-Eastern Asia', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 145: 'Western Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_all = pd.concat([df_new_15,df_new_18], axis=1)
df_all.to_csv('data/5_3_1_Women_Married_Union_15_18_SDG_Regions.csv', index=True)

#5.3.2 FGM SDG Regions (GQN6n)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_STA_FGMS.15+202.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={15: 'Northern Africa', 202: 'Sub-Saharan Africa'},inplace=True)
df_new.to_csv('data/5_3_2_FGM_SDG_Regions.csv', index=True)

#5.3.2 FGM legal protection Nordics (84qt0)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/GIDDB2019/ALL.DNK+FIN+ISL+NOR+SWE.AIC.RPI_FGM_LAW/all?startTime=2019&endTime=2019'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Year', columns='Country', values='Value')
df_new.to_csv('data/5_3_2_FGM_Legal_Protection_Nordics.csv', index=True)

#5.4.1 Gender gap unpaid work Nordics (BOfnW)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/TIME_USE/DNK+FIN+NOR+SWE.UPW.WOMEN+MEN.15_64.LY/all?'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Sex', columns='Country', values='Value')
df_new.loc['Gender gap'] = df_new.loc['Women'] - df_new.loc['Men'] 
df_new.insert(4, "OECD", [0,0,127])
df_new.to_csv('data/5_4_1_Gender_Gap_Unpaid_Work_Nordics.csv', index=True)

#5.5.1 Women share of seats in national parliaments and local governemnts World (y4jTH)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_LOCGELS+SG_GEN_PARL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={'SG_GEN_LOCGELS':'Local government'}, inplace=True)
df_new.rename(index={'SG_GEN_PARL':'National parliaments'}, inplace=True)
df_new.to_csv('data/5_5_1_Women_Share_Parliaments_Local_Governments_World_Total.csv', index=True)

#5.5.1 Women share of seats in national parliaments SDG regions (3sA1h)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_PARL.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/5_5_1_Women_Share_Parliaments_SDG_Regions.csv', index=True)

#5.5.1 Women share of seats in local governments SDG regions (LdV5e)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_LOCGELS.53+543+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/5_5_1_Women_Share_Local_Governments_SDG_Regions.csv', index=True)

#5.5.1 Women share of seats in national parliaments Nordics (cJ0lO)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_PARL.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/5_5_1_Women_Share_Parliaments_Nordics.csv', index=True)

#5.5.1 Women share of seats in local governments Nordics (KByGf)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_LOCGELS.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/5_5_1_Women_Share_Local_Governments_Nordics.csv', index=True)

#5.5.2 Women share of manegerial positions World (PbvZ1)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..IC_GEN_MGTL.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/5_5_2_Women_Share_Manegerial_Positions_World_Total.csv', index=True)

#5.5.2 Women share of manegerial positions SDG Regions (s520P)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..IC_GEN_MGTL.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/5_5_2_Women_Share_Manegerial_Positions_SDG_Regions.csv', index=True)

#5.5.2 Women share manegerial positions Nordics (FPtnC)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..IC_GEN_MGTL.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2018-01-01&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/5_5_2_Women_Share_Manegerial_Positions_Nordics.csv', index=True)

#5.6.1 Full and equal access World and SDG Regions (3S8v0)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_LGR_ACSRHE+SH_LGR_ACSRHES1+SH_LGR_ACSRHES2+SH_LGR_ACSRHES3+SH_LGR_ACSRHES4.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new = df_new.reindex(columns=['World','Europe and Northern America','Northern Africa and Western Asia','Sub-Saharan Africa','Central and Southern Asia','Eastern and South-Eastern Asia','Australia and New Zealand','Oceania*','Latin America and the Caribbean'])
df_new.rename(index={'SH_LGR_ACSRHE': 'Total','SH_LGR_ACSRHES1':'Maternity Care','SH_LGR_ACSRHES2':'Contraceptive Services','SH_LGR_ACSRHES3':'Sexuality Education','SH_LGR_ACSRHES4':'HIV and HPV'},inplace=True)
df_new.to_csv('data/5_6_1_Full_Equal_Access_World_SDG_Regions.csv', index=True)

#5.6.1 Full and equal access Nordics (WD61C)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SH_LGR_ACSRHE+SH_LGR_ACSRHES1+SH_LGR_ACSRHES2+SH_LGR_ACSRHES3+SH_LGR_ACSRHES4.208+246+352+578+752.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='SERIES', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(index={'SH_LGR_ACSRHE': 'Total','SH_LGR_ACSRHES1':'Maternity Care','SH_LGR_ACSRHES2':'Contraceptive Services','SH_LGR_ACSRHES3':'Sexuality Education','SH_LGR_ACSRHES4':'HIV and HPV'},inplace=True)
df_new.to_csv('data/5_6_1_Full_Equal_Access_Nordics.csv', index=True)

#5.b.1 Women internet use last 3m Nordics (vK8gz)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/ICT_HH2/DNK+FIN+ISL+NOR+SWE.C5B.F_Y16_74/all?startTime=2005&endTime=2021'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Time', columns='Country', values='Value')
df_new1 = df_new.loc[[2005, 2021]]
df_new1.to_csv('data/5_b_1_Women_Internet_Use_3M_Nordics.csv', index=True)

#5.b.1 Women internet use almost daily last 3m Nordics (Wml4d)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/ICT_HH2/DNK+FIN+ISL+NOR+SWE.C5B1.F_Y16_74/all?startTime=2005&endTime=2021'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Time', columns='Country', values='Value')
df_new1 = df_new.loc[[2005, 2021]]
df_new1.to_csv('data/5_b_1_Women_Internet_Use_Daily_Nordics.csv', index=True)

#5.b.1 Women vs Men internet use almost daily Nordics (RQZPd)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/ICT_HH2/DNK+FIN+ISL+NOR+SWE.C5B1.F_Y16_74+M_Y16_74/all?startTime=2021&endTime=2021'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=pd.read_csv(io.StringIO(result.text))
df_new = df.pivot(index='Breakdowns', columns='Country', values='Value')
df_new.to_csv('data/5_b_1_Women_Men_Internet_Use_Daily_Nordics.csv', index=True)

#5.c.1 Share of countries track and make allocations gender equality and women empowerment World and SDG Regions (Gf28o)
df_csv = pd.read_csv('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.8/..SG_GEN_EQPWN.1+53+543+62+513+747+753+202+419.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543:'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/5_c_1_Track_Make_Allications_World_SDG_Regions.csv', index=True)

