#!/usr/bin/env python3

from glob import glob
from sys import exit

result_file = 'CWB_sta_num.list'
others_output = 'CWB_sta_num.list'

## assume there's no existed filelist
pfile_list = sorted(glob('./Pfiles/*.?16'))

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

#with open(result_file, 'w') as f:
#    #for i in sitename_dict:
#    for key,value in sitename_dict.items():
#        f.write(f'{key:4s} : {value:2d}\n')

import re

reverse_dict = dict()
with open(others_output) as f:
    ff = sorted(f.readlines())
    if len(ff) != len(sitename_dict):
        print('\x1b[1;33;41mPlease Check Number of Sites!\x1b[0m')
    for key,value in sorted(sitename_dict.items()):
        for i in ff:
            if bool(re.search(f'{key}',i)):
                if key in reverse_dict.keys():
                    continue
                if bool(re.search(f'{value}',i)):
                    next_index = re.search(f'{value}',i).span()[1]
                    next_char = i[next_index]
                    if bool(re.match('[0-9]',next_char)):
                        print(f'{key:4s}: \x1b[1;31mPlease Check!\x1b[0m')
                    print(f'{key:4s}: \x1b[1;32mCorrect!\x1b[0m')
                    reverse_dict[key] = reverse_dict.get(key, 0) + 1
                else:
                    print(f'{key:4s}: \x1b[1;31mPlease Check!\x1b[0m')
