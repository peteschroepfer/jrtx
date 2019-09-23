import numpy as np
import pandas as pd
from collections import Counter

types = {'Transaction Date':str,'Posted Date':str, 'Card No':int,
    'Description':str,'Category':str,'Debit':float, 'Credit':float}
filepath = 'testcsv'
df = pd.read_csv(filepath, dtype=types)

Desc = list(map(str,list(df['Description'])))

gs_stations = ('CHEVRON', '7 ', '7-', "SHELL","QUIK STOP", "76",
    "CORNER STORE",'EXXONMOBIL','OCEAN 76','COSTCO GAS','TEXACO',
    'SAV ON GASOLINE','AMERICAN GASOLINE','BOULDER CREEK AMERICAN', 'KWIK SERVE GAS',
    'CORNERSTONE AUTO SERVIC','ROD & ROS GAS/FOOD MART #')

full_food = {}

half_food = {}

tmp_list = []
for item in Desc:
    if str(item).startswith(gs_stations):
        tmp_list.append('GAS')
    elif str(item).startswith('SAFEWAY'):
        tmp_list.append('SAFEWAY')
    elif str(item).startswith('SAN LORENZO'):
        tmp_list.append('SAN LORENZO')
    elif str(item).startswith('EXPEDIA'):
        tmp_list.append('EXPEDIA')
    else:
        tmp_list.append(item)

Desc = tmp_list
df['Description'] = Desc

des_dict = {}

for item in tmp_list:
    if item in des_dict:
        des_dict[item] += 1
    else:
        des_dict[item] = 1

for key,value in des_dict.items():
    print(key+',')
