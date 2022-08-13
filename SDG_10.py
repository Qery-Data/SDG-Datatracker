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