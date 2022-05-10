#!/usr/bin/env python3

input_file = './hw12_material/CWB202104.DAT'

with open(input_file) as f:
    all_lines = f.readlines()

day_list = []
for each_event in all_lines:
    day   = int(each_event[6:8].strip()) 
    day_list.append(day)

day_dict = dict()
for day_element in sorted(day_list):
    day_dict[day_element] = day_dict.get(day_element, 0) + 1

day_cum_dict = dict()
day_cum_value = 0
for day_element in sorted(day_dict.keys()):
    day_cum_value = day_cum_value + day_dict[day_element]
    day_cum_dict[day_element] = day_cum_value

#### print
import matplotlib.pyplot as plt

days_info=list(day_dict.keys())
count_info=list(day_dict.values())                                                                                                                                                                 

plt.plot(days_info, count_info,'o:', color='deepskyblue', lw=2, label='Seismicity')
plt.axis([min(days_info), max(days_info), 0, max(count_info)])
plt.legend()
plt.title('2021 04 Seismicity', fontsize = 16)
plt.xlabel('Numbers of EQs'   , fontsize = 12)
plt.ylabel('day of 2021 Apr'  , fontsize = 12)
plt.show()

days_cum_info=list(day_cum_dict.keys())
count_cum_info=list(day_cum_dict.values())                                                                                                                                                                 

plt.plot(days_cum_info, count_cum_info, color='black', lw=2, label='Cumulative EQs')
plt.axis([min(days_cum_info), max(days_cum_info), 0, max(count_cum_info)])
plt.legend()
plt.title('2021 04 Cumulative EQs'  , fontsize = 18)
plt.xlabel('Cumulative # of EQs'    , fontsize = 14)
plt.ylabel('day of 2021 Apr'        , fontsize = 14)
plt.show()
