#!/usr/bin/env python3

###################################### HW8-1

#### Functions for HW3-2
### 攝氏轉華氏
def celsius_to_fahrenheit(degree_celsius_origin: float) -> float:
    degree_fahrenheit = degree_celsius_origin * ( 9 / 5 ) + 32
    return degree_fahrenheit

### 華氏轉攝氏
def fahrenheit_to_celsius(degree_fahrenheit_origin: float) -> float:
    degree_celsius =  ( degree_fahrenheit_origin - 32 ) * ( 5 / 9 )
    return degree_celsius

while True:
    input_temperature = input('Enter a temperature value (e.g. 94.87C or 94.87F); or just Enter to finish:')
    if input_temperature == '':
        break
    if input_temperature[-1] == 'C':
        temp_type = 'Celsius'
        temp_type_symbol='C'
    elif input_temperature[-1] == 'F':
        temp_type = 'Fahrenheit'
        temp_type_symbol='F'
    else:
        print('please use capital C or F!')
        continue
    try:
        input_temp_number = float(input_temperature[:-1])
    except:
        print(f'Value error:could not convert string to float: {input_temperature[:-1]}')
        continue
    if temp_type == 'Celsius':
        result_temp = celsius_to_fahrenheit(input_temp_number)
    else:
        result_temp = fahrenheit_to_celsius(input_temp_number)
    print(f'{input_temperature} is {result_temp:.2f}{temp_type_symbol}')
    break

################################################# HW8-2

from collections import namedtuple

Evdata = namedtuple("Evdata", "evtime evlon evlat evdep evmag")

evdata_list = []

with open('hw08_material/USGS_20200928_20201028.csv') as f:
    ff=f.readlines()

Evdata = namedtuple("Evdata", "evtime evlon evlat evdep evmag")
event_list = []

for i in ff[1:]:
    evtime,evlat,evlon,evdep,evmag=i.strip().split(',')[:5]
    #print(time,lon,lat,depth,evmag)
    evlon=float(evlon)
    evlat=float(evlat)
    evdep=float(evdep)
    evmag=float(evmag)
    if( evdep >= 50 and evmag > 5.0 ):
        event_list.append(Evdata(evtime,evlon,evlat,evdep,evmag))

with open('hw08_material/EQ_50km_M6.txt','w+') as fff:
    for item in event_list:
        #print(f'{item.evtime} {item.evlon:9.4f} {item.evlat:8.4f} {item.evdep:6.2f} {item.evmag:3.1f}')
        fff.write(f'{item.evtime} {item.evlon:9.4f} {item.evlat:8.4f} {item.evdep:6.2f} {item.evmag:3.1f}\n')
