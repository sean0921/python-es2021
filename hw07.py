#!/usr/bin/env python3

def is_valid_2d_matrix(input_list: list) -> bool:
    if type(input_list) != list:
        return False
    for i in range(0,len(input_list)):
        if len(input_list[i] != input_list[0]):
            return False
        if len(input_list[i][0]) != 1:
            return False
    return True

def check_outer_product_available(matrix_list_1: list, matrix_list_2: list) -> bool:
    if ( not is_valid_2d_matrix(matrix_list_1) ) or ( not is_valid_2d_matrix(matrix_list_2) ):
        return False
    if len(matrix_list_1[0]) != len(matrix_list_2):
        return False
    return True

def matrix_outer_product(matrix_list_1: list, matrix_list_2: list) -> list:
    # 先產生 size 對的空陣列並且補 0
    matrix_result = []
    for i in range( 0, len(matrix_list_1) ):
        matrix_result.append([])
        for m in range( 0, len(matrix_list_2[0]) ):
            matrix_result[i].append(0)
    #matrix_result[0][0] = \
    #          matrix_list_1[0][0] * matrix_list_2[0][0] \
    #        + matrix_list_1[1][0] * matrix_list_2[0][1] \
    #        + matrix_list_1[2][0] * matrix_list_2[0][2] \
    #        #....
    #        + matrix_list_1[len(matrix_list_1)][0] * matrix_list_2[0][len(matrix_list_2[0])]
    #for i in range( 0, len(matrix_list_1) ):
    #    for j in range( 0, len(matrix_list_1[i]) ):
    #        for n in range( 0, len(matrix_list_2[m]) ):
    #            for m in range( 0, len(matrix_list_2[0]) ):
    #                if j == n:
    #                    matrix_result[i][m] += matrix_list_1[i][j] * matrix_list_2[n][m]
    for i in range( 0, len(matrix_list_1) ):
        for j in range( 0, len(matrix_list_1[i]) ):
            for m in range( 0, len(matrix_list_2[0]) ):
                matrix_result[i][m] += matrix_list_1[i][j] * matrix_list_2[j][m]
    return matrix_result

def year_is_yun(year: int) -> bool:
    if year % 4 != 0:
        return False
    if ( year % 100 == 0 ) and ( year % 400 != 0):
        return False
    return True

def days_in_year(year: int) -> int:
    if year_is_yun(year) == True:
        return 366
    else:
        return 365

def month_days_list(year: int) -> list:
    if year_is_yun(year) == True:
        month_list = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        month_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    return month_list

def ymd_to_yearjday(year: int, month: int, day: int):
    jday = 0
    for i in range(0,month-1):
        jday += month_days_list(year)[i]
    jday += day
    return year,jday

def yearjday_to_ymd(year: int, julian_day: int):
    i=0
    month=1
    day=julian_day
    while True:
        julian_day -= month_days_list(year)[i]
        if julian_day > 0:
            month+=1
            i+=1
            day=julian_day
            continue
        else:
            break
    return year,month,day

################################ HW 7-1

matrix_a = [ 
        [2, 4, 6],
        [9, 9, 0],
        [6, 2, 3],
        [7, 1, 8],
]
matrix_b = [ 
        [7, 0, 2],
        [9, 2, 8],
        [6, 1, 6],
]

print(matrix_outer_product(matrix_a,matrix_b))

## verify
#import numpy as np
#print(np.matmul(np.array(matrix_a), np.array(matrix_b)))


################################ HW 7-2

print(ymd_to_yearjday(2016,11,2))
print(yearjday_to_ymd(2017,123))

## verify
#from obspy import UTCDateTime
#print(UTCDateTime(2016,11,2).julday)
#print(UTCDateTime(year=2017,julday=123))
