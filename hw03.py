#!/usr/bin/env python3

#### Functions for HW1
### 球體體積公式
def ball_volume(radius: float) -> float:
    from math import pi
    volume_ball = ( 4 / 3 ) * pi * radius ** 3  ## formula of ball volume
    return volume_ball

### 輸出體積結果的函式
def print_ball_volume_ans_msg(radius: float):
    volume_of_ball = ball_volume(radius)
    print("The total volume of the ball with", radius ,"cm radius is", volume_of_ball, "cm^3")

#### Functions for HW2
### 攝氏轉華氏
def celsius_to_fahrenheit(degree_celsius_origin: float) -> float:
    degree_fahrenheit = degree_celsius_origin * ( 9 / 5 ) + 32
    return degree_fahrenheit

### 華氏轉攝氏
def fahrenheit_to_celsius(degree_fahrenheit_origin: float) -> float:
    degree_celsius =  ( degree_fahrenheit_origin - 32 ) * ( 5 / 9 )
    return degree_celsius

#### Functions for HW3
### 每個橫線骨架的單位 (不含開頭)
def single_horizontal_bone() -> str:
    return '-' * 4 + '+'

### 每個垂直骨架方格的單位 (不含開頭)
def single_vertical_bone() -> str:
    return ' ' * 4 + '|'

### 列印出可調整橫線單位寬度的骨架
def print_horizontal_bone(bone_length: int):
    print('+' + single_horizontal_bone() * bone_length )

### 列印出可調整直線方格單位寬度的骨架
def print_vertical_bone(bone_length: int):
    print('|' + single_vertical_bone() * bone_length)

#############

print("HW1:")
print_ball_volume_ans_msg(5)
print_ball_volume_ans_msg(13)
print_ball_volume_ans_msg(41)
print_ball_volume_ans_msg(396)
total_volume = ball_volume(5) + ball_volume(13) + ball_volume(41) + ball_volume(396)
print("Total volume of four balls are", total_volume, "cm^3")
print("")

print("HW2:")
print(100, 'degree in Fahrenheit is', fahrenheit_to_celsius(100), 'degree in Celsius')
print(100, 'degree in Celsius is', celsius_to_fahrenheit(100), 'degree in Fahrenheit ')

print("HW3:")
print_horizontal_bone(2)
print_vertical_bone(2)
print_vertical_bone(2)
print_vertical_bone(2)
print_horizontal_bone(2)
print_vertical_bone(2)
print_vertical_bone(2)
print_vertical_bone(2)
print_horizontal_bone(2)


"""

output

HW1:
The total volume of the ball with 5 cm radius is 523.5987755982989 cm^3
The total volume of the ball with 13 cm radius is 9202.7720799157 cm^3
The total volume of the ball with 41 cm radius is 288695.60970408283 cm^3
The total volume of the ball with 396 cm radius is 260120252.6024979 cm^3
Total volume of four balls are 260418674.5830575 cm^3

HW2:
100 degree in Fahrenheit is 37.77777777777778 degree in Celsius
100 degree in Celsius is 212.0 degree in Fahrenheit 
HW3:
+----+----+
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
+----+----+


"""