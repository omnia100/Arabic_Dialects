# -*- coding: utf-8 -*-
"""Data Fetching.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JJ5VcuPdkjSKjzg2Gg0_7hAO2SvuLju_
"""

import pandas as pd
import json
import os
import requests
import codecs

# !gdown --id 1TMvKuU4eYyEWXu4vWcNPODcEs_bOJ_lY

directory_path = '/content/ids/'

os.makedirs(directory_path, exist_ok=True)

df = pd.read_csv('dialect_dataset.csv')

"""## split ID's file into smaller files"""

n = df.shape[0]

i=0
while True:
  if n-i < 1000:
    df['id'][i:].astype(str).to_json(f'{directory_path}{i}.json', "values")
    break

  df['id'][i:i+1000].astype(str).to_json(f'{directory_path}{i}.json', "values")
  i+=1000

"""## send data request for each file"""

api_url = 'https://recruitment.aimtechnologies.co/ai-tasks'

jsonObj = {}
# i=0
with os.scandir(directory_path) as entries:
    for entry in entries:
      with open(f'{directory_path}{entry.name}') as json_file:
        dataDict = json.load(json_file)
        dataStr = json.dumps(dataDict)
        r = requests.post(api_url, data=dataStr)
        jsonObj.update(r.json())
        # i+=1
        # if i==2:
        #   break

"""## save recieved data in dataframe"""

# for k, v in r.json().items():
#   print(k, ": ", v)

df_api = pd.DataFrame(jsonObj, index=['text'])

df_api = df_api.T

df_api.index.rename('id',inplace=True)

df_api.reset_index(level=0, inplace=True)

df_api['id'] = df_api['id'].astype(int)

"""## merge"""

df_final = df_api.merge(df,on='id')

"""## save dataframe as a json file in drive"""

with open('df.json', 'w', encoding='utf-8') as file:
    df_final.to_json(file, force_ascii=False)

"""## copy to drive"""

# from google.colab import drive
# drive.mount('/content/drive')

# !cp df.json /content/drive/MyDrive