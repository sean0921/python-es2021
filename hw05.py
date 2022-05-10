#!/usr/bin/env python3

from typing import Tuple
import turtle
import math

cwb_webpage = '''<ul style="display: block;" class="Report"><h3>地震</h3><li class="levOne"><a href="/V7/earthquake/quake_index.htm" class="Earthquake10">最近地震</a></li><li class="levOne"><a href="/V7/earthquake/rtd_eq.htm" class="Earthquake20">地震活動彙整</a></li><li class="levOne"><a href="/V7/earthquake/quake_world.htm" class="Earthquake30">全球地震</a></li><li class="levOne"><a href="/V7/knowledge/encyclopedia/eq000.htm" class="Earthquake40">地震百問</a></li><li class="levOne"><a href="/V7/earthquake/research.htm" class="Earthquake50">技術報告</a></li><li class="levOne"><a href="/V7/earthquake/accsta.htm" class="Earthquake60">測站</a></li><li class="levOne"><a href="/V7/earthquake/quake_preparedness.htm" class="Earthquake70">地震防護</a></li><li class="levOne"><a href="/V7/earthquake/damage_eq.htm" class="Earthquake80">災害地震</a></li><li class="levOne"><a href="/V7/earthquake/talk.htm" class="Earthquake90">地震話題</a></li></ul>'''

cwb_webpage2 = ''' <meta name="msapplication-square70x70logo" content="/V7/images/win10/cwbPinlogo70.png"><meta name="msapplication-square150x150logo" content="/V7/images/win10/cwbPinlogo150.png">'''

def find_url(input_str: str,input_index: int) -> Tuple[int, str]:
    url_format_feature_start = 'a href="'
    url_format_feature_end = '"'
    a_basic = input_str.find(url_format_feature_start,input_index)
    a = a_basic + len(url_format_feature_start)
    b = input_str.find(url_format_feature_end,a)
    if a_basic == -1:
        return None,-1
    else:
        url_content = input_str[a:b]
        next_index_start = b + 1
        return url_content, next_index_start

def print_found_string(input_str):
    this_url=''
    next_index=0
    while True:
        this_url,next_index=find_url(input_str,next_index)
        if next_index == -1:
            print('Game is over!')
            break
        else:
            print(this_url)

def myploygon(num_ploy,len_ploy):
    for i in range(num_ploy):
        turtle.forward(len_ploy)
        turtle.left(360/num_ploy)

def mycircle(radius_circle):
    myploygon(60,2*math.pi*radius_circle/60)

print('')
print('Homework 5-1')
print('')

print('cwb_webpage: ')
print_found_string(cwb_webpage)
print('')

print('cwb_webpage2: ')
print_found_string(cwb_webpage2)
print('')
print('')

mycircle(float(input('請輸入你想要的圓形半徑: ')))
