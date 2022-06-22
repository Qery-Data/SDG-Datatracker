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

#2_1
url = "https://api.datawrapper.de/v3/charts?folderId=104896&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_1 = []
for i in json_object['list']:
        chart_list_2_1.append(i['publicId'])

#2_2
url = "https://api.datawrapper.de/v3/charts?folderId=104912&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_2 = []
for i in json_object['list']:
        chart_list_2_2.append(i['publicId'])

#2_4
url = "https://api.datawrapper.de/v3/charts?folderId=104915&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_4 = []
for i in json_object['list']:
        chart_list_2_4.append(i['publicId'])

#2_5
url = "https://api.datawrapper.de/v3/charts?folderId=104920&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_5 = []
for i in json_object['list']:
        chart_list_2_5.append(i['publicId'])

#2_a
url = "https://api.datawrapper.de/v3/charts?folderId=104981&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_a = []
for i in json_object['list']:
        chart_list_2_a.append(i['publicId'])

#2_b
url = "https://api.datawrapper.de/v3/charts?folderId=105014&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_b = []
for i in json_object['list']:
        chart_list_2_b.append(i['publicId'])

#2_c
url = "https://api.datawrapper.de/v3/charts?folderId=105025&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_2_c = []
for i in json_object['list']:
        chart_list_2_c.append(i['publicId'])

#Publish
chart_list_2_all = (chart_list_2_1 + chart_list_2_2 + chart_list_2_4 + chart_list_2_5 + chart_list_2_a + chart_list_2_b + chart_list_2_c)
for vars in chart_list_2_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#3_1
url = "https://api.datawrapper.de/v3/charts?folderId=105285&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_1 = []
for i in json_object['list']:
        chart_list_3_1.append(i['publicId'])

#3_2
url = "https://api.datawrapper.de/v3/charts?folderId=105295&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_2 = []
for i in json_object['list']:
        chart_list_3_2.append(i['publicId'])

#3_3
url = "https://api.datawrapper.de/v3/charts?folderId=106111&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_3 = []
for i in json_object['list']:
        chart_list_3_3.append(i['publicId'])

#3_4
url = "https://api.datawrapper.de/v3/charts?folderId=106683&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_4 = []
for i in json_object['list']:
        chart_list_3_4.append(i['publicId'])

#3_5
url = "https://api.datawrapper.de/v3/charts?folderId=106710&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_5 = []
for i in json_object['list']:
        chart_list_3_5.append(i['publicId'])

#3_6
url = "https://api.datawrapper.de/v3/charts?folderId=106729&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_6 = []
for i in json_object['list']:
        chart_list_3_6.append(i['publicId'])

#3_7
url = "https://api.datawrapper.de/v3/charts?folderId=107115&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_7 = []
for i in json_object['list']:
        chart_list_3_7.append(i['publicId'])

#3_8
url = "https://api.datawrapper.de/v3/charts?folderId=107117&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_8 = []
for i in json_object['list']:
        chart_list_3_8.append(i['publicId'])

#3_9
url = "https://api.datawrapper.de/v3/charts?folderId=107314&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_9 = []
for i in json_object['list']:
        chart_list_3_9.append(i['publicId'])

#3_a
url = "https://api.datawrapper.de/v3/charts?folderId=107322&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_a = []
for i in json_object['list']:
        chart_list_3_a.append(i['publicId'])

#3_b
url = "https://api.datawrapper.de/v3/charts?folderId=107325&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_b = []
for i in json_object['list']:
        chart_list_3_b.append(i['publicId'])

#3_c
url = "https://api.datawrapper.de/v3/charts?folderId=107349&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_c = []
for i in json_object['list']:
        chart_list_3_c.append(i['publicId'])

#3_d
url = "https://api.datawrapper.de/v3/charts?folderId=107362&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_3_d = []
for i in json_object['list']:
        chart_list_3_d.append(i['publicId'])

#Publish
chart_list_3_all = (chart_list_3_1 + chart_list_3_2 + chart_list_3_3 + chart_list_3_4 + chart_list_3_5 + chart_list_3_6 + chart_list_3_7 + chart_list_3_8 + chart_list_3_9 + chart_list_3_a + chart_list_3_b + chart_list_3_c + chart_list_3_d)
for vars in chart_list_3_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)