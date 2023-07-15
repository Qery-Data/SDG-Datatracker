from pyjstat import pyjstat
import requests
import os
import json
import time
from datetime import datetime
import locale
import io
import pandas as pd
os.makedirs('data', exist_ok=True)
access_token = os.getenv('DW_TOKEN')

def robust_data_download(url, max_retries=5, delay_between_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # will raise an HTTPError if the response was unsuccessful
            content = response.content  # store the content
        except requests.exceptions.HTTPError as err:
            if response.status_code == 503 and attempt < max_retries - 1:  # it's a 503 error and we have more retries left
                print(f"Server responded with 503 Service Unavailable. Retrying in {delay_between_retries} seconds...")
                time.sleep(delay_between_retries)  # wait before retrying
                continue
            else:  # it's a different error or we have no retries left
                raise SystemExit(err)
        break

    # If we got a successful response, we can convert it to a pandas DataFrame
    df_csv = pd.read_csv(io.StringIO(content.decode('utf-8')))

    return df_csv


#3.1.1 Maternal mortlity ratio World (GSN09)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_MORT.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_World_Total.csv', index=True)

#3.1.1 Maternal mortlity ratio SDG regions (ldsu3)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_MORT.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_SDG_Regions.csv', index=True)

#3.1.1 Maternal mortality ratio Nordics (f97NM) 
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_MORT.208+246+352+578+752.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_1_1_Maternal_Mortality_Ratio_Nordics.csv', index=True)

#3.1.1 Delivery coverage World (PURO4)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_BRTC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_World_Total.csv', index=True)

#3.1.1 Delivery coverage World (PURO4)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_BRTC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_World_Total.csv', index=True)

#3.1.1 Delivery coverage SDG regions (Nyj1B)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_BRTC.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_DETAIL', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_SDG_Regions.csv', index=True)

#3.1.1 Delivery coverage Nordics (bUwlZ)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_BRTC.208+246+352+578+752............../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_DETAIL', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_1_1_Delivery_Coverage_Nordics.csv', index=True)

#3.2.1 Child mortality (under 5 years) World (nlIg9)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_MORT.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_World_Total.csv', index=True)

#3.2.1 Child mortality (under 5 years) SDG regions (cjeVd)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_MORT.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_SDG_Regions.csv', index=True)

#3.2.1 Child mortality (under 5 years) Nordics (w7m0C)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_MORT.208+246+352+578+752._T........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_2_1_Child_Mortality_Under5_Nordics.csv', index=True)

#3.2.1 Infant Mortality World (nf9Av)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_IMRT.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_2_1_Infant_Mortality_World_Total.csv', index=True)

#3.2.1 Infant Mortality SDG regions (fH5V4)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_IMRT.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_2_1_Infant_Mortality_SDG_Regions.csv', index=True)

#3.2.1 Infant mortality rate Nordics (ExhV2)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_IMRT.208+246+352+578+752._T........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_2_1_Infant_Mortality_Nordics.csv', index=True)

#3.2.2 Neonatal Mortality World (RDJVM)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_NMRT.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_2_2_Neonatal_Mortality_World_Total.csv', index=True)

#3.2.2 Neonatal Mortality SDG regions (iWaE0)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_NMRT.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_2_2_Neonatal_Mortality_SDG_Regions.csv', index=True)

#3.2.2 Neonatal mortality Nordics (FhHAO)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DYN_NMRT.208+246+352+578+752._T........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_2_2_Neonatal_Mortality_Nordics.csv', index=True)

#3.3.1 HIV World (YEUyr)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_HIV_INCD.1._T._T........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_3_1_HIV_World_Total.csv', index=True)

#3.3.1 HIV SDG regions (qS6FC)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_HIV_INCD.53+62+513+543+747+753+202+419._T._T........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_3_1_HIV_SDG_Regions.csv', index=True)

#3.3.1 HIV Nordics (6U375)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_HIV_INCD.208+246+352+578+752._T._T........./ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_3_1_HIV_Nordics.csv', index=True)

#3.3.1 AIDS (OECD) Nordics (aq4jB)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_STAT/COMDAIDS.NEWCASTX.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_3_1_AIDS_Nordics.csv', index=True)

#3.3.2 Tuberculosis World (6YipF)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TBS_INCD.1._T._T........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_3_2_Tuberculosis_World_Total.csv', index=True)

#3.3.2 Tuberculosis SDG regions (FIwuf)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TBS_INCD.53+62+513+543+747+753+202+419._T._T........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_3_2_Tuberculosis_SDG_Regions.csv', index=True)

#3.3.2 Tuberculosis Nordics (ZjTWN)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TBS_INCD.208+246+352+578+752._T._T........./ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_3_2_Tuberculosis_Nordics.csv', index=True)

#3.3.2 Tuberculosis Deaths (OECD) Nordics (0yqie)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_STAT/CICDTBLS.TXCMILTX.DNK+FIN+ISL+NOR+SWE/all?startTime=2000&endTime=2020'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_3_2_Tuberculosis_Deaths_Nordics.csv', index=True)

#3.3.3 Malaria World (QJyrP)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_MALR.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_3_3_Malaria_World_Total.csv', index=True)

#3.3.3 Malaria SDG regions (c6s34)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_MALR.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_3_3_Malaria_SDG_Regions.csv', index=True)

#3.3.4 Hepatitis B World (hW80b)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_HAP_HBSAG.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_3_4_Hepatitis_B_World_Total.csv', index=True)

#3.3.4 Hepatitis B SDG regions (349RP)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_HAP_HBSAG.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_3_4_Hepatitis_B_SDG_Regions.csv', index=True)

#3.3.4 Hepatitis B (OECD) Nordics (8ENns)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_STAT/COMDIHPB.PERCMTTX.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_3_4_Hepatitis_B_Nordics.csv', index=True)

#3.3.5 Tropical diseases World (e2fLz)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TRP_INTVN.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_3_5_Tropical_Diseases_World_Total.csv', index=True)

#3.3.5 Tropical diseases SDG regions (M85pk)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TRP_INTVN.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_3_5_Tropical_Diseases_SDG_Regions.csv', index=True)

#3.3.5 Tropical diseases Nordics (KDmB7)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_TRP_INTVN.208+246+352+578+752.........../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_3_5_Tropical_Diseases_Nordics.csv', index=True)

#3.4.1 Deaths NCDs World (lgWv7)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DTH_NCD.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='COMPOSITE_BREAKDOWN', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_4_1_Deaths_NCD_World_Total.csv', index=True)

#3.4.1 Mortality rate NCDs World (ZqTo1)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DTH_NCOM.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_4_1_Mortality_Rate_NCD_World_Total.csv', index=True)

#3.4.1 Mortality rate NCDs SDG regions (v6Fkv)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DTH_NCOM.53+62+513+543+747+753+202+419._T............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_4_1_Mortality_Rate_NCD_SDG_Regions.csv', index=True)

#3.4.1 Mortality rate NCDs Nordics (dB9cQ)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_DTH_NCOM.208+246+352+578+752._T............/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_4_1_Mortality_Rate_NCD_Nordics.csv', index=True)

#3.4.1 Suicide mortality rate World (Xq9N3)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_SCIDE.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_4_1_Suicide_Mortality_Rate_World_Total.csv', index=True)

#3.4.1 Suicide mortality rate SDG regions (ceJJ1)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_SCIDE.53+62+513+543+747+753+202+419._T............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_4_1_Suicide_Mortality_Rate_SDG_Regions.csv', index=True)

#3.4.1 Suicide mortality rate Nordics (28v58)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_SCIDE.208+246+352+578+752._T............/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_4_1_Suicide_Mortality_Rate_Nordics.csv', index=True)

#3.5.2 Alcohol consumption World (33cLP)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ALC_CONSPT.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_5_2_Alcohol_Consumption_World_Total.csv', index=True)

#3.5.2 Alcohol consumption SDG regions (hQSq1)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ALC_CONSPT.53+62+513+543+747+753+202+419._T............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_5_2_Alcohol_Consumption_SDG_Regions.csv', index=True)

#3.5.2 Alcohol consumption (OECD) Nordics (JlAkV)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_LVNG/ACOLALCT.LIPPERNB.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_5_2_Alcohol_Consumption_Nordics.csv', index=True)

#3.6.1 Road traffic deaths World (EWs55)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_TRAF.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_6_1_Road_traffic_deaths_World_Total.csv', index=True)

#3.6.1 Road traffic deaths SDG regions (ybzj2)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_TRAF.53+62+513+543+747+753+202+419._T............/ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_6_1_Road_traffic_deaths_SDG_Regions.csv', index=True)

#3.6.1 Road traffic deaths Nordics OECD (bOwUi)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/IRTAD_CASUAL_BY_AGE/DNK+FIN+ISL+NOR+SWE.KIL.TOT.TOT.RATE-POP-100T.CORRECTED/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_6_1_Road_Traffic_Deaths_Nordics.csv', index=True)

#3.7.1 Women Family Planning World (7ZvbI)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_FPL_MTMM.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_7_1_Women_Family_Planning_World_Total.csv', index=True)

#3.7.1 Women Family Planning SDG regions (V3T88)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_FPL_MTMM.53+62+513+543+747+753+202+419............../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_7_1_Women_Family_Planning_SDG_Regions.csv', index=True)

#3.7.1 Adolescent birth rate World (SLabG)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SP_DYN_ADKL.1..Y15T19........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_7_2_Adolescent_Birth_Rate_World_Total.csv', index=True)

#3.7.2 Adolescent Birth Rate SDG regions (uRSmS)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SP_DYN_ADKL.53+62+513+543+747+753+202+419..Y15T19........./ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_7_2_Adolescent_Birth_Rate_SDG_Regions.csv', index=True)

#3.7.2 Adolescent fertility rate OECD (jNvOV)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/FAMILY/DNK+FIN+ISL+NOR+SWE.TOTAL.FAM20/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_7_2_Adolescent_Fertility_Rate_Nordics.csv', index=True)

#3.8.1 Universal Health Care Index World (DUq5f)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_UNHC.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_8_1_Universal_Health_Care_Index_World_Total.csv', index=True)

#3.8.1 Universal Health Care Index SDG regions (DUq5f)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_UNHC.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_8_1_Universal_Health_Care_Index_SDG_Regions.csv', index=True)

#3.8.1 Universal Health Care Index Nordics (8JurX)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_UNHC.208+246+352+578+752............../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_8_1_Universal_Health_Care_Index_Nordics.csv', index=True)

#3.8.2 Share Large Health Expenditure SDG regions (zgnG7)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_XPD_EARN10.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_8_2_Share_Large_Health_Expenditure_SDG_Regions.csv', index=True)

#3.9.1 Mortality Household and air pollution SDG regions (tvmPS)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_ASAIRP.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_9_1_Mortality_Household_Air_Pollution_SDG_Regions.csv', index=True)

#3.9.1 Household and air pollution Nordics (TrVi1)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_ASAIRP.208+246+352+578+752............../ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_9_1_Mortality_Household_Air_Pollution_Nordics.csv', index=True)

#3.9.2 WASH SDG regions (Ub8Mb)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_WASHARI.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America',543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_9_2_Mortality_WASH_SDG_Regions.csv', index=True)

#3.9.2 WASH Nordics (xxxxx)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_WASHARI.208+246+352+578+752.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_9_2_Mortality_WASH_Nordics.csv', index=True)

#3.9.3 Mortality unintentional posioning World (9k8OW)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_POISN.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_9_3_Mortality_Unintentional_Posioning_World_Total.csv', index=True)

#3.9.3 Mortality unintentional posioning SDG regions (VKShu)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_STA_POISN.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_9_3_Mortality_Unintentional_Posioning_SDG_Regions.csv', index=True)

#3.9.3 Mortality Accidental poisoning Nordics OECD (Au6rM)
oecd_url='https://stats.oecd.org/SDMX-JSON/data/HEALTH_STAT/CICDPOSN.TXCMILTX.DNK+FIN+ISL+NOR+SWE/all?startTime=2000'
result = requests.get(oecd_url, headers={'Accept': 'text/csv'})
df=robust_data_download(oecd_url)
df_new = df.pivot(index='Country', columns='Year', values='Value')
df_new.to_csv('data/3_9_3_Mortality_Accidental_Poisoning_Nordics.csv', index=True)

#3.a.1 Prevalence tobacco World (qSHFT)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_PRV_SMOK.1._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_a_1_Prevalence_Tobacco_World_Total.csv', index=True)

#3.a.1 Prevalence Tobacco SDG regions (yoBzM)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_PRV_SMOK.53+62+513+543+747+753+202+419._T........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_a_1_Prevalence_Tobacco_SDG_Regions.csv', index=True)

#3.a.1 Prevalence Tobacco Nordics (us4AE)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_PRV_SMOK.208+246+352+578+752._T............/ALL/?detail=full&startPeriod=2000-01-01&dimensionAtObservation=TIME_PERIOD&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.to_csv('data/3_a_1_Prevalence_Tobacco_Nordics.csv', index=True)

#3.b.1 DTP3 World (UMgHK)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_DTP3.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_b_1_DTP3_World_Total.csv', index=True)

#3.b.1 MCV2 World (1vKaz)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_MCV2.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_b_1_MCV2_World_Total.csv', index=True)

#3.b.1 PCV3 World (8j9KU)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_PCV3.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_b_1_PCV3_World_Total.csv', index=True)

#3.b.1 HPV World (zhPGz)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_HPV.1.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World'}, inplace=True)
df_new.to_csv('data/3_b_1_HPV_World_Total.csv', index=True)

#3.b.1 DTP3 SDG regions (sBPJS)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_DTP3.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_b_1_DTP3_SDG_Regions.csv', index=True)

#3.b.1 MCV2 SDG regions (4PrPX)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_MCV2.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_b_1_MCV2_SDG_Regions.csv', index=True)

#3.b.1 PCV3 SDG regions (M1UgK)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_PCV3.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_b_1_PCV3_SDG_Regions.csv', index=True)

#3.b.1 HPV SDG regions (yPNKH)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_HPV.53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='TIME_PERIOD', columns='REF_AREA', values='OBS_VALUE')
df_new.rename(columns={53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new.to_csv('data/3_b_1_HPV_SDG_Regions.csv', index=True)

#3.b.1 DTP3/MCV2/PCV3/HPV Nordics (hLWW4)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_DTP3.208+246+352+578+752............./ALL/?detail=full&lastNObservations=1&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df2_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_MCV2.208+246+352+578+752............./ALL/?detail=full&lastNObservations=1&format=csv")
df2_new = df2_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df2_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df3_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_PCV3.208+246+352+578+752............./ALL/?detail=full&lastNObservations=1&format=csv")
df3_new = df3_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df3_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df4_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_ACS_HPV.208+246+352+578+752._T............/ALL/?detail=full&lastNObservations=1&format=csv")
df4_new = df4_csv.pivot(index='REF_AREA', columns='SERIES', values='OBS_VALUE')
df4_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_all = pd.concat([df_new,df2_new,df3_new,df4_new],axis=1)
df_all.to_csv('data/3_b_1_DTP3_MCV2_PCV3_HPV_Nordics.csv', index=True)

#3.b.2 Net ODA Health Total (0WKD3)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..DC_TOF_HLTHNT.515.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={515:'Total'}, inplace=True)
df_new.to_csv('data/3_b_2_Net_ODA_Health_Total.csv', index=True)

#3.c.1 Health Worker Density Total (Z4XdO)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_MED_DEN.1+9+150+15+21+30+34+35+143+145+202.........../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='OCCUPATION', values='OBS_VALUE')
df_new.rename(index={1:'World',9:'Oceania',150:'Europe',15:'Northern Africa',21:'Northern America',30:'Eastern Asia',34:'Southern Asia',35:'South-Eastern Asia',143:'Central Asia',145:'Western Asia',202:'Sub-Saharan Africa' }, inplace=True)
df_new.rename(columns={'ISCO08_221':'Medical doctors','ISCO08_222_322':'Nursing and midwifery personnel', 'ISCO08_2261':'Dentists','ISCO08_2262':'Pharmacists'}, inplace=True)
df_new.to_csv('data/3_c_1_Health_Worker_Density_Total.csv', index=True)

#3.c.1 Health Worker Density Medical Doctors Nordics (dhEhe)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_MED_DEN.208+246+352+578+752......ISCO08_221...../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'ISCO08_221':'Medical doctors','ISCO08_222_322':'Nursing and midwifery personnel', 'ISCO08_2261':'Dentists','ISCO08_2262':'Pharmacists'}, inplace=True)
df_new.to_csv('data/3_c_1_Health_Worker_Density_Medical_Doctors_Nordics.csv', index=True)

#3.c.1 Health Worker Density Nursing and midwifery personnel Nordics (INMP2)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_MED_DEN.208+246+352+578+752......ISCO08_222_322...../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'ISCO08_221':'Medical doctors','ISCO08_222_322':'Nursing and midwifery personnel', 'ISCO08_2261':'Dentists','ISCO08_2262':'Pharmacists'}, inplace=True)
df_new.to_csv('data/3_c_1_Health_Worker_Density_Nursing_Midwifery_Nordics.csv', index=True)

#3.c.1 Health Worker Density Dentists Nordics (ILcaX)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_MED_DEN.208+246+352+578+752......ISCO08_2261...../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'ISCO08_221':'Medical doctors','ISCO08_222_322':'Nursing and midwifery personnel', 'ISCO08_2261':'Dentists','ISCO08_2262':'Pharmacists'}, inplace=True)
df_new.to_csv('data/3_c_1_Health_Worker_Density_Dentists_Nordics.csv', index=True)

#3.c.1 Health Worker Density Pharmacists Nordics (dLEdy)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_MED_DEN.208+246+352+578+752......ISCO08_2262...../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new.rename(columns={'ISCO08_221':'Medical doctors','ISCO08_222_322':'Nursing and midwifery personnel', 'ISCO08_2261':'Dentists','ISCO08_2262':'Pharmacists'}, inplace=True)
df_new.to_csv('data/3_c_1_Health_Worker_Density_Pharmacists_Nordics.csv', index=True)

#3.d.1 IHR Capacity SDG regions (FoXOI)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_IHR_CAPS.1+53+62+513+543+747+753+202+419........SPAR2_C01+SPAR2_C02+SPAR2_C03+SPAR2_C04+SPAR2_C05+SPAR2_C06+SPAR2_C07+SPAR2_C08+SPAR2_C09+SPAR2_C10+SPAR2_C11+SPAR2_C12+SPAR2_C13+SPAR2_C14+SPAR2_C15.../ALL/?detail=full&lastNObservations=1&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='COMPOSITE_BREAKDOWN', values='OBS_VALUE')
df_new.rename(index={1: 'World', 53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'},inplace=True)
df_new['Average'] = df_new.mean(numeric_only=True, axis=1)
df_new.to_csv('data/3_d_1_IHR_SDG_Regions.csv', index=True)

#3.d.1 IHR Capacity Nordics (O4iVQ)
df_csv = robust_data_download("https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_IHR_CAPS.208+246+352+578+752........SPAR2_C01+SPAR2_C02+SPAR2_C03+SPAR2_C04+SPAR2_C05+SPAR2_C06+SPAR2_C07+SPAR2_C08+SPAR2_C09+SPAR2_C10+SPAR2_C11+SPAR2_C12+SPAR2_C13+SPAR2_C14+SPAR2_C15.../ALL/?detail=full&lastNObservations=1&format=csv")
df_new = df_csv.pivot(index='REF_AREA', columns='COMPOSITE_BREAKDOWN', values='OBS_VALUE')
df_new.rename(index={208: 'Denmark', 246: 'Finland', 352: 'Iceland', 578:'Norway',752:'Sweden'},inplace=True)
df_new['Average'] = df_new.mean(numeric_only=True, axis=1)
df_new.to_csv('data/3_d_1_IHR_Nordics.csv', index=True)

#3.d.2 MRSA Total (f03pp)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_BLD_MRSA.1+53+62+513+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/3_d_2_MRSA_Total.csv', index=True)

#3.d.2 ECOLI World (HUWGr)
df_csv = robust_data_download('https://data.un.org/ws/rest/data/IAEG-SDGs,DF_SDG_GLH,1.12/..SH_BLD_ECOLI.1+53+62+513+543+747+753+202+419.........../ALL/?detail=full&dimensionAtObservation=TIME_PERIOD&format=csv')
df_new = df_csv.pivot(index='REF_AREA', columns='TIME_PERIOD', values='OBS_VALUE')
df_new.rename(index={1:'World',53: 'Australia and New Zealand', 62: 'Central and Southern Asia', 202: 'Sub-Saharan Africa', 419: 'Latin America and the Caribbean', 513: 'Europe and Northern America', 543: 'Oceania*', 747: 'Northern Africa and Western Asia', 753: 'Eastern and South-Eastern Asia'}, inplace=True)
df_new.to_csv('data/3_d_2_ECOLI_Total.csv', index=True)