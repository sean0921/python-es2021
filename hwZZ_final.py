#!/usr/bin/env python3

from hwZZ_finalL46081028 import weight_avg, word_dict

#### Question 1
weight_avg('hwZZ_material/class_grad.txt', 'hwZZ_material/grade_w1.txt')
weight_avg('hwZZ_material/class_grad.txt', 'hwZZ_material/grade_w2.txt', w1=2, w3=4)


#### Question 2
word_dict('hwZZ_material/I_have_a_dream.txt', 'hwZZ_material/text_dict.txt', sort_num=False)
word_dict('hwZZ_material/I_have_a_dream.txt', 'hwZZ_material/text_dict_num.txt', sort_num=True)


#### Question 3
input_filename = 'hwZZ_material/2012_2020_M3EQ.cvs'

import matplotlib.pyplot as plt
from collections import namedtuple

EQ_data = namedtuple('EQ_data','year mon dy hr minutes seconds lon lat dep mag evid')

with open(input_filename) as f:
    input_contents = f.readlines()[1:]

EQ_data_list = []
for each_line in input_contents:
    year,mon,dy,hr,minutes,seconds,lon,lat,dep,mag,evid=each_line.strip('\n').split(',')
    EQ_data_list.append(EQ_data(year,mon,dy,hr,minutes,seconds,lon,lat,dep,mag,evid))

year_dict = dict()
mag_list = []
depth_list = []

for item in EQ_data_list:
    year_dict[item.year] = year_dict.get(item.year, 0) + 1
    mag_list.append(float(item.mag))
    depth_list.append(float(item.dep))

year_count_year  = list(year_dict.keys())
year_count_count = list(year_dict.values())

year_cum_dict = dict()
year_cum_value = 0 
for year_element in sorted(year_dict.keys()):
    year_cum_value = year_cum_value + year_dict[year_element]
    year_cum_dict[year_element] = year_cum_value

plt.figure(figsize=(12,12))

plt.subplot(2,2,1)
plt.title('2012 ~ 2020 seismicity (bar)')
plt.bar(year_count_year, year_count_count, 0.8)
plt.ylim([0, 2000])
plt.xlabel('year')
plt.ylabel('# of earthquakes')

year_cum_info=list(year_cum_dict.keys())
count_cum_info=list(year_cum_dict.values())

plt.subplot(2,2,2)
plt.title('2012 ~ 2020 Cumulative earthquake')
plt.plot(year_cum_info, count_cum_info, 'o--' )
plt.xlabel('year')
plt.ylabel('# of earthquakes')

plt.subplot(2,2,3)
plt.title('Magnitude of earthquake (hist)')
plt.hist(mag_list, bins=25)
plt.xlabel('Magnitude')
plt.ylabel('Number of EQs')

plt.subplot(2,2,4)
plt.title('Depth of earthquake (hist)')
plt.hist(depth_list, bins=25)
plt.xlabel('Depth (km)')
plt.ylabel('Number of EQs')

#plt.show()
plt.savefig('mpl_pyplot_output.png')

