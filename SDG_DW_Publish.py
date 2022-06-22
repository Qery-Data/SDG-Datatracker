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

#1_1
url = "https://api.datawrapper.de/v3/charts?folderId=102479&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_1 = []
for i in json_object['list']:
        chart_list_1_1.append(i['publicId'])

#1_2
url = "https://api.datawrapper.de/v3/charts?folderId=102480&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_2 = []
for i in json_object['list']:
        chart_list_1_2.append(i['publicId'])

#1_3
url = "https://api.datawrapper.de/v3/charts?folderId=102484&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_3 = []
for i in json_object['list']:
        chart_list_1_3.append(i['publicId'])

#1_4
url = "https://api.datawrapper.de/v3/charts?folderId=102492&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_4 = []
for i in json_object['list']:
        chart_list_1_4.append(i['publicId'])

#1_5
url = "https://api.datawrapper.de/v3/charts?folderId=102495&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_5 = []
for i in json_object['list']:
        chart_list_1_5.append(i['publicId'])

#1_a
url = "https://api.datawrapper.de/v3/charts?folderId=102727&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_1_a = []
for i in json_object['list']:
        chart_list_1_a.append(i['publicId'])

#Publish
chart_list_1_all = (chart_list_1_1 + chart_list_1_2 + chart_list_1_3 + chart_list_1_4 + chart_list_1_5 + chart_list_1_a)
for vars in chart_list_1_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)