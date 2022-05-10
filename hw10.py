#!/usr/bin/env python3

from glob import glob

result_file = './hw10_material/CWB_sta_num.list'

## assume there's no existed filelist
pfile_list = sorted(glob('./hw10_material/Pfiles/*.?16'))

readings = []

for pfile_name in pfile_list:
    with open(pfile_name) as f:          
        readings.extend(f.readlines()[1:])

sitename_list = []
for each_reading in readings:
    sitename = each_reading[1:5].strip()
    sitename_list.append(sitename)

sitename_dict = dict()
for sitename_element in sorted(sitename_list):
    sitename_dict[sitename_element] = sitename_dict.get(sitename_element, 0) + 1

print(sitename_dict)

with open(result_file, 'w') as f:
    #for i in sitename_dict:
    for key,value in sitename_dict.items():
        f.write(f'{key:4s} : {value:2d}\n') 
