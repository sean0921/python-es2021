#!/usr/bin/env python3

from collections import namedtuple

EQ_data = namedtuple('EQ_data','year month day hour minute second latitude longitude depth magnitude')
EQ_data_list = []

with open('./hw13_material/CWB_202010EQ_info.DAT') as f:
    contents = f.readlines()

for content in contents:
    year   = int(content[0:4])
    month  = int(content[4:6])
    day    = int(content[6:8])
    hour   = int(content[8:10])
    minute = int(content[10:12])
    second = float(content[12:18])
    lat_degree = int(content[18:20])
    lat_minute = float(content[20:25])
    latitude = lat_degree + lat_minute / 60
    lon_degree = int(content[25:28])
    lon_minute = float(content[28:33])
    longitude = lon_degree + lon_minute / 60
    depth = float(content[33:39])
    magnitude = float(content[39:43])
    EQ_data_list.append(EQ_data(year,month,day,hour,minute,second,latitude,longitude,depth,magnitude))

lat_list = []
lon_list = []
mag_list = []
day_dict = dict()

list_L_1p5   = []
list_1p5_2p0 = []
list_2p0_3p0 = []
list_3p0_4p0 = []
list_4p0_H   = []

for item in EQ_data_list:
    if item.magnitude > 2.5:
        lat_list.append(item.latitude)
        lon_list.append(item.longitude)
    day_dict[item.day] = day_dict.get(item.day, 0) + 1
    mag_list.append(item.magnitude)

    if item.magnitude <= 1.5:
        list_L_1p5.append(item.magnitude)
    elif 1.5 < item.magnitude <= 2.0:
        list_1p5_2p0.append(item.magnitude)
    elif 2.0 < item.magnitude <= 3.0:
        list_2p0_3p0.append(item.magnitude)
    elif 3.0 < item.magnitude <= 4.0:
        list_3p0_4p0.append(item.magnitude)
    #if item.magnitude > 4.0:
    else:
        list_4p0_H.append(item.magnitude)

#print(list_L_1p5,
#      list_1p5_2p0,
#      list_2p0_3p0,
#      list_3p0_4p0,
#      list_4p0_H)

number_L_1p5    = len(list_L_1p5)
number_1p5_2p0  = len(list_1p5_2p0)
number_2p0_3p0  = len(list_2p0_3p0)
number_3p0_4p0  = len(list_3p0_4p0)
number_4p0_H    = len(list_4p0_H)

day_count_day   = list(day_dict.keys())
day_count_count = list(day_dict.values())

#print(lat_list, lon_list, day_dict)


############################

import matplotlib.pyplot as plt

#xx = [1, 2, 3, 4, 5, 6]
#yy = [3, 5, 2, 8, 7, 4]
plt.figure(figsize=(12,12))

plt.subplot(2,2,1)
plt.title('2020 10 Earthquake M > 2.5 (scatter)')
plt.scatter(lon_list, lat_list, 12, 'r', '*')
plt.xlim([min(lon_list), max(lon_list)])
plt.xlabel('Longitude')
plt.ylim([min(lat_list), max(lat_list)])
plt.ylabel('Latitude')
plt.grid()  # grid

plt.subplot(2,2,2)
plt.title('2020 10 Seismicity (bar)')
plt.bar(day_count_day, day_count_count, 0.8)
print(day_count_day, day_count_count, 0.8)
plt.xlim([min(day_count_day), max(day_count_day) ])
plt.xlabel('day of 2020 Oct')
#plt.ylim([min(day_count_count), max(day_count_count)])
plt.ylim([min(day_count_count), round( max(day_count_count)/10 )*10 ])
plt.ylabel('Number of EQs')

plt.subplot(2,2,3)
plt.title('2020 10 magnitude (hist)')
plt_hist_info = plt.hist(mag_list, 20)
plt.xlim(min(plt_hist_info[1]), max(plt_hist_info[1]))
plt.xlabel('Magnitude')
plt.ylim(0, max(plt_hist_info[0]*1.05))
plt.ylabel('Number of EQs')

plt.subplot(2,2,4)
routine = ['<= 1.5'    , '1.5 < M <= 2.0', '2.0 < M <= 3.0', '3.0 < M <= 4.0', '> 4.0']
number  = [number_L_1p5, number_1p5_2p0  , number_2p0_3p0  , number_3p0_4p0  , number_4p0_H]

plt.title('2020 10 Pie of Magnitudes')
plt.pie(number, labels = routine)
#plt.savefig('myfig.jpg',bbox_inches='tight')
plt.show()
