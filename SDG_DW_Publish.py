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

#4_1
url = "https://api.datawrapper.de/v3/charts?folderId=108821&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_1 = []
for i in json_object['list']:
        chart_list_4_1.append(i['publicId'])

#4_2
url = "https://api.datawrapper.de/v3/charts?folderId=108909&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_2 = []
for i in json_object['list']:
        chart_list_4_2.append(i['publicId'])

#4_3
url = "https://api.datawrapper.de/v3/charts?folderId=108910&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_3 = []
for i in json_object['list']:
        chart_list_4_3.append(i['publicId'])

#4_4
url = "https://api.datawrapper.de/v3/charts?folderId=108911&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_4 = []
for i in json_object['list']:
        chart_list_4_4.append(i['publicId'])

#4_5
url = "https://api.datawrapper.de/v3/charts?folderId=108968&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_5 = []
for i in json_object['list']:
        chart_list_4_5.append(i['publicId'])

#4_6
url = "https://api.datawrapper.de/v3/charts?folderId=109048&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_6 = []
for i in json_object['list']:
        chart_list_4_6.append(i['publicId'])

#4_7
url = "https://api.datawrapper.de/v3/charts?folderId=109052&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_7 = []
for i in json_object['list']:
        chart_list_4_7.append(i['publicId'])

#4_a
url = "https://api.datawrapper.de/v3/charts?folderId=109100&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_a = []
for i in json_object['list']:
        chart_list_4_a.append(i['publicId'])

#4_b
url = "https://api.datawrapper.de/v3/charts?folderId=109107&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_b = []
for i in json_object['list']:
        chart_list_4_b.append(i['publicId'])

#4_c
url = "https://api.datawrapper.de/v3/charts?folderId=109114&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_4_c = []
for i in json_object['list']:
        chart_list_4_c.append(i['publicId'])

#Publish
chart_list_4_all = (chart_list_4_1 + chart_list_4_2 + chart_list_4_3 + chart_list_4_4 + chart_list_4_5 + chart_list_4_6 + chart_list_4_7 + chart_list_4_a + chart_list_4_b + chart_list_4_c)
for vars in chart_list_4_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#5_1
url = "https://api.datawrapper.de/v3/charts?folderId=110448&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_1 = []
for i in json_object['list']:
        chart_list_5_1.append(i['publicId'])

#5_2
url = "https://api.datawrapper.de/v3/charts?folderId=110448&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_2 = []
for i in json_object['list']:
        chart_list_5_2.append(i['publicId'])

#5_3
url = "https://api.datawrapper.de/v3/charts?folderId=110467&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_3 = []
for i in json_object['list']:
        chart_list_5_3.append(i['publicId'])

#5_4
url = "https://api.datawrapper.de/v3/charts?folderId=110523&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_4 = []
for i in json_object['list']:
        chart_list_5_4.append(i['publicId'])

#5_5
url = "https://api.datawrapper.de/v3/charts?folderId=110531&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_5 = []
for i in json_object['list']:
        chart_list_5_5.append(i['publicId'])

#5_6
url = "https://api.datawrapper.de/v3/charts?folderId=110639&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_6 = []
for i in json_object['list']:
        chart_list_5_6.append(i['publicId'])

#5_b
url = "https://api.datawrapper.de/v3/charts?folderId=110668&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_b = []
for i in json_object['list']:
        chart_list_5_b.append(i['publicId'])

#5_c
url = "https://api.datawrapper.de/v3/charts?folderId=110667&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_5_c = []
for i in json_object['list']:
        chart_list_5_c.append(i['publicId'])

#Publish
chart_list_5_all = (chart_list_5_1 + chart_list_5_2 + chart_list_5_3 + chart_list_5_4 + chart_list_5_5 + chart_list_5_6 + chart_list_5_b + chart_list_5_c)
for vars in chart_list_5_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#6_1
url = "https://api.datawrapper.de/v3/charts?folderId=110808&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_1 = []
for i in json_object['list']:
        chart_list_6_1.append(i['publicId'])

#6_2
url = "https://api.datawrapper.de/v3/charts?folderId=110812&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_2 = []
for i in json_object['list']:
        chart_list_6_2.append(i['publicId'])

#6_3
url = "https://api.datawrapper.de/v3/charts?folderId=110883&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_3 = []
for i in json_object['list']:
        chart_list_6_3.append(i['publicId'])

#6_4
url = "https://api.datawrapper.de/v3/charts?folderId=110947&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_4 = []
for i in json_object['list']:
        chart_list_6_4.append(i['publicId'])

#6_5
url = "https://api.datawrapper.de/v3/charts?folderId=110953&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_5 = []
for i in json_object['list']:
        chart_list_6_5.append(i['publicId'])

#6_6
url = "https://api.datawrapper.de/v3/charts?folderId=110955&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_6 = []
for i in json_object['list']:
        chart_list_6_6.append(i['publicId'])

#6_a
url = "https://api.datawrapper.de/v3/charts?folderId=110980&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_a = []
for i in json_object['list']:
        chart_list_6_a.append(i['publicId'])

#6_b
url = "https://api.datawrapper.de/v3/charts?folderId=110985&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_6_b = []
for i in json_object['list']:
        chart_list_6_b.append(i['publicId'])

#Publish
chart_list_6_all = (chart_list_6_1 + chart_list_6_2 + chart_list_6_3 + chart_list_6_4 + chart_list_6_5 + chart_list_6_6 + chart_list_6_a + chart_list_6_b)
for vars in chart_list_6_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#7_1
url = "https://api.datawrapper.de/v3/charts?folderId=111344&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_7_1 = []
for i in json_object['list']:
        chart_list_7_1.append(i['publicId'])

#7_2
url = "https://api.datawrapper.de/v3/charts?folderId=111352&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_7_2 = []
for i in json_object['list']:
        chart_list_7_2.append(i['publicId'])

#7_3
url = "https://api.datawrapper.de/v3/charts?folderId=111365&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_7_3 = []
for i in json_object['list']:
        chart_list_7_3.append(i['publicId'])

#7_a
url = "https://api.datawrapper.de/v3/charts?folderId=111366&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_7_a = []
for i in json_object['list']:
        chart_list_7_a.append(i['publicId'])

#7_b
url = "https://api.datawrapper.de/v3/charts?folderId=111368&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_7_b = []
for i in json_object['list']:
        chart_list_7_b.append(i['publicId'])

#Publish
chart_list_7_all = (chart_list_7_1 + chart_list_7_2 + chart_list_7_3 + chart_list_7_a + chart_list_7_b)
for vars in chart_list_7_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#8_1
url = "https://api.datawrapper.de/v3/charts?folderId=111612&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_1 = []
for i in json_object['list']:
        chart_list_8_1.append(i['publicId'])

#8_2
url = "https://api.datawrapper.de/v3/charts?folderId=111624&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_2 = []
for i in json_object['list']:
        chart_list_8_2.append(i['publicId'])

#8_3
url = "https://api.datawrapper.de/v3/charts?folderId=111631&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_3 = []
for i in json_object['list']:
        chart_list_8_3.append(i['publicId'])

#8_4
url = "https://api.datawrapper.de/v3/charts?folderId=111648&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_4 = []
for i in json_object['list']:
        chart_list_8_4.append(i['publicId'])

#8_5
url = "https://api.datawrapper.de/v3/charts?folderId=111670&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_5 = []
for i in json_object['list']:
        chart_list_8_5.append(i['publicId'])

#8_6
url = "https://api.datawrapper.de/v3/charts?folderId=111678&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_6 = []
for i in json_object['list']:
        chart_list_8_6.append(i['publicId'])

#8_7
url = "https://api.datawrapper.de/v3/charts?folderId=111681&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_7 = []
for i in json_object['list']:
        chart_list_8_7.append(i['publicId'])

#8_8
url = "https://api.datawrapper.de/v3/charts?folderId=111743&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_8 = []
for i in json_object['list']:
        chart_list_8_8.append(i['publicId'])

#8_9
url = "https://api.datawrapper.de/v3/charts?folderId=111757&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_9 = []
for i in json_object['list']:
        chart_list_8_9.append(i['publicId'])

#8_10
url = "https://api.datawrapper.de/v3/charts?folderId=111765&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_10 = []
for i in json_object['list']:
        chart_list_8_10.append(i['publicId'])

#8_a
url = "https://api.datawrapper.de/v3/charts?folderId=111770&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_a = []
for i in json_object['list']:
        chart_list_8_a.append(i['publicId'])

#8_b
url = "https://api.datawrapper.de/v3/charts?folderId=111771&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_8_b = []
for i in json_object['list']:
        chart_list_8_b.append(i['publicId'])

#Publish
chart_list_8_all = (chart_list_8_1 + chart_list_8_2 + chart_list_8_3 + chart_list_8_4 + chart_list_8_5 + chart_list_8_6 + chart_list_8_7 + chart_list_8_8 + chart_list_8_9 + chart_list_8_10 + chart_list_8_a + chart_list_8_b)
for vars in chart_list_8_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#9_2
url = "https://api.datawrapper.de/v3/charts?folderId=112328&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_2 = []
for i in json_object['list']:
        chart_list_9_2.append(i['publicId'])

#9_3
url = "https://api.datawrapper.de/v3/charts?folderId=112342&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_3 = []
for i in json_object['list']:
        chart_list_9_3.append(i['publicId'])

#9_4
url = "https://api.datawrapper.de/v3/charts?folderId=112345&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_4 = []
for i in json_object['list']:
        chart_list_9_4.append(i['publicId'])

#9_5
url = "https://api.datawrapper.de/v3/charts?folderId=112361&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_5 = []
for i in json_object['list']:
        chart_list_9_5.append(i['publicId'])

#9_a
url = "https://api.datawrapper.de/v3/charts?folderId=112461&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_a = []
for i in json_object['list']:
        chart_list_9_a.append(i['publicId'])

#9_b
url = "https://api.datawrapper.de/v3/charts?folderId=112462&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_b = []
for i in json_object['list']:
        chart_list_9_b.append(i['publicId'])

#9_c
url = "https://api.datawrapper.de/v3/charts?folderId=112465&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_9_c = []
for i in json_object['list']:
        chart_list_9_c.append(i['publicId'])

#Publish
chart_list_9_all = (chart_list_9_2 + chart_list_9_3 + chart_list_9_4 + chart_list_9_5 + chart_list_9_a + chart_list_9_b + chart_list_9_c)
for vars in chart_list_9_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#10_1
url = "https://api.datawrapper.de/v3/charts?folderId=113713&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_1 = []
for i in json_object['list']:
        chart_list_10_1.append(i['publicId'])

#10_2
url = "https://api.datawrapper.de/v3/charts?folderId=113714&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_2 = []
for i in json_object['list']:
        chart_list_10_2.append(i['publicId'])

#10_3
url = "https://api.datawrapper.de/v3/charts?folderId=113716&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_3 = []
for i in json_object['list']:
        chart_list_10_3.append(i['publicId'])

#10_4
url = "https://api.datawrapper.de/v3/charts?folderId=113717&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_4 = []
for i in json_object['list']:
        chart_list_10_4.append(i['publicId'])

#10_5
url = "https://api.datawrapper.de/v3/charts?folderId=113749&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_5 = []
for i in json_object['list']:
        chart_list_10_5.append(i['publicId'])

#10_6
url = "https://api.datawrapper.de/v3/charts?folderId=113750&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_6 = []
for i in json_object['list']:
        chart_list_10_6.append(i['publicId'])

#10_7
url = "https://api.datawrapper.de/v3/charts?folderId=113784&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_7 = []
for i in json_object['list']:
        chart_list_10_7.append(i['publicId'])

#10_a
url = "https://api.datawrapper.de/v3/charts?folderId=114570&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_a = []
for i in json_object['list']:
        chart_list_10_a.append(i['publicId'])

#10_b
url = "https://api.datawrapper.de/v3/charts?folderId=114571&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_b = []
for i in json_object['list']:
        chart_list_10_b.append(i['publicId'])

#10_c
url = "https://api.datawrapper.de/v3/charts?folderId=114572&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_10_c = []
for i in json_object['list']:
        chart_list_10_c.append(i['publicId'])

#Publish
chart_list_10_all = (chart_list_10_1 + chart_list_10_2 + chart_list_10_3 + chart_list_10_4 + chart_list_10_5 + chart_list_10_6 + chart_list_10_7 + chart_list_10_a + chart_list_10_b + chart_list_10_c)
for vars in chart_list_10_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#11_1
url = "https://api.datawrapper.de/v3/charts?folderId=114603&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_1 = []
for i in json_object['list']:
        chart_list_11_1.append(i['publicId'])

#11_2
url = "https://api.datawrapper.de/v3/charts?folderId=114641&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_2 = []
for i in json_object['list']:
        chart_list_11_2.append(i['publicId'])

#11_3
url = "https://api.datawrapper.de/v3/charts?folderId=114682&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_3 = []
for i in json_object['list']:
        chart_list_11_3.append(i['publicId'])

#11_6
url = "https://api.datawrapper.de/v3/charts?folderId=114647&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_6 = []
for i in json_object['list']:
        chart_list_11_6.append(i['publicId'])

#11_7
url = "https://api.datawrapper.de/v3/charts?folderId=114662&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_7 = []
for i in json_object['list']:
        chart_list_11_7.append(i['publicId'])

#11_a
url = "https://api.datawrapper.de/v3/charts?folderId=114678&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_11_a = []
for i in json_object['list']:
        chart_list_11_a.append(i['publicId'])

#Publish
chart_list_11_all = (chart_list_11_1 + chart_list_11_2 + chart_list_11_3 + chart_list_11_6 + chart_list_11_7 + chart_list_11_a)
for vars in chart_list_11_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#12_1
url = "https://api.datawrapper.de/v3/charts?folderId=115423&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_1 = []
for i in json_object['list']:
        chart_list_12_1.append(i['publicId'])

#12_2
url = "https://api.datawrapper.de/v3/charts?folderId=115424&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_2 = []
for i in json_object['list']:
        chart_list_12_2.append(i['publicId'])

#12_3
url = "https://api.datawrapper.de/v3/charts?folderId=115425&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_3 = []
for i in json_object['list']:
        chart_list_12_3.append(i['publicId'])

#12_4
url = "https://api.datawrapper.de/v3/charts?folderId=115428&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_4 = []
for i in json_object['list']:
        chart_list_12_4.append(i['publicId'])

#12_6
url = "https://api.datawrapper.de/v3/charts?folderId=115436&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_6 = []
for i in json_object['list']:
        chart_list_12_6.append(i['publicId'])

#12_8
url = "https://api.datawrapper.de/v3/charts?folderId=115437&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_8 = []
for i in json_object['list']:
        chart_list_12_8.append(i['publicId'])

#12_a
url = "https://api.datawrapper.de/v3/charts?folderId=115438&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_a = []
for i in json_object['list']:
        chart_list_12_a.append(i['publicId'])

#12_c
url = "https://api.datawrapper.de/v3/charts?folderId=115443&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_12_c = []
for i in json_object['list']:
        chart_list_12_c.append(i['publicId'])

#Publish
chart_list_12_all = (chart_list_12_1 + chart_list_12_2 + chart_list_12_3 + chart_list_12_4 + chart_list_12_6 + chart_list_12_8 + chart_list_12_a + chart_list_12_c)
for vars in chart_list_12_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#13_2
url = "https://api.datawrapper.de/v3/charts?folderId=115699&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_13_2 = []
for i in json_object['list']:
        chart_list_13_2.append(i['publicId'])

#13_3
url = "https://api.datawrapper.de/v3/charts?folderId=115733&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_13_3 = []
for i in json_object['list']:
        chart_list_13_3.append(i['publicId'])

#13_a
url = "https://api.datawrapper.de/v3/charts?folderId=115741&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_13_a = []
for i in json_object['list']:
        chart_list_13_a.append(i['publicId'])

#Publish
chart_list_13_all = (chart_list_13_2 + chart_list_13_3 + chart_list_13_a)
for vars in chart_list_13_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#14_1
url = "https://api.datawrapper.de/v3/charts?folderId=116897&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_1 = []
for i in json_object['list']:
        chart_list_14_1.append(i['publicId'])

#14_2
url = "https://api.datawrapper.de/v3/charts?folderId=117389&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_2 = []
for i in json_object['list']:
        chart_list_14_2.append(i['publicId'])

#14_4
url = "https://api.datawrapper.de/v3/charts?folderId=118068&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_4 = []
for i in json_object['list']:
        chart_list_14_4.append(i['publicId'])

#14_5
url = "https://api.datawrapper.de/v3/charts?folderId=118312&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_5 = []
for i in json_object['list']:
        chart_list_14_5.append(i['publicId'])

#14_6
url = "https://api.datawrapper.de/v3/charts?folderId=118313&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_6 = []
for i in json_object['list']:
        chart_list_14_6.append(i['publicId'])

#14_7
url = "https://api.datawrapper.de/v3/charts?folderId=118345&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_7 = []
for i in json_object['list']:
        chart_list_14_7.append(i['publicId'])

#14_a
url = "https://api.datawrapper.de/v3/charts?folderId=118358&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_a = []
for i in json_object['list']:
        chart_list_14_a.append(i['publicId'])

#14_b
url = "https://api.datawrapper.de/v3/charts?folderId=118360&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_14_b = []
for i in json_object['list']:
        chart_list_14_b.append(i['publicId'])

#Publish
chart_list_14_all = (chart_list_14_1 + chart_list_14_2 + chart_list_14_4 + chart_list_14_5 + chart_list_14_6 + chart_list_14_7 + chart_list_14_a + chart_list_14_b)
for vars in chart_list_14_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)

#15_1
url = "https://api.datawrapper.de/v3/charts?folderId=118532&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_1 = []
for i in json_object['list']:
        chart_list_15_1.append(i['publicId'])

#15_2
url = "https://api.datawrapper.de/v3/charts?folderId=119096&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_2 = []
for i in json_object['list']:
        chart_list_15_2.append(i['publicId'])

#15_4
url = "https://api.datawrapper.de/v3/charts?folderId=119099&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_4 = []
for i in json_object['list']:
        chart_list_15_4.append(i['publicId'])

#15_5
url = "https://api.datawrapper.de/v3/charts?folderId=119141&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_5 = []
for i in json_object['list']:
        chart_list_15_5.append(i['publicId'])

#15_6
url = "https://api.datawrapper.de/v3/charts?folderId=119169&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_6 = []
for i in json_object['list']:
        chart_list_15_6.append(i['publicId'])

#15_a
url = "https://api.datawrapper.de/v3/charts?folderId=119179&order=DESC&orderBy=createdAt&limit=100&offset=0&expand=false"
headers = {
    "Authorization": ("Bearer " + access_token),
    "Accept": "*/*"
    }
response = requests.get(url, headers=headers)
json_object = json.loads(response.text)
chart_list_15_a = []
for i in json_object['list']:
        chart_list_15_a.append(i['publicId'])

#Publish
chart_list_15_all = (chart_list_15_1 + chart_list_15_2 + chart_list_15_4 + chart_list_15_5 + chart_list_15_6 + chart_list_15_a)
for vars in chart_list_15_all:
    url = "https://api.datawrapper.de/v3/charts/" + vars + '/publish/'
    headers = {
        "Authorization": ("Bearer " + access_token),
        "Accept": "*/*"
        }
    response = requests.request("POST", url, headers=headers)