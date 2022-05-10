#!/usr/bin/env python3

print('############################################################################')
print('')

### Homework 1

print('HW1 Result:')
print('')

radius = 5  ## unit: cm
pi_number = 3.1415926535 ## approach numberic value
volume_ball = ( 4 / 3 ) * pi_number * radius ** 3  ## formula of ball volume

print('The volume of ball is (cm^3):',volume_ball)

##### split
print('')
print('############################################################################')
print('')
####

### Homework 2

print('HW2 Result:')
print('')

deposit_pricipal = 100000
deposit_rate = 1.5 * 0.01  ## 1.5%
deposit_number = 5 ## assume each year is one

deposit_total = deposit_pricipal * ( (1 + deposit_rate) ** deposit_number )

print('The total deposit is:', deposit_total)

##### split
print('')
print('############################################################################')
print('')
####

### Homework 3

print('HW3 Result:')
print('')

degree_fahrenheit_origin = 100
degree_celsius_origin = 100

degree_celsius =  ( degree_fahrenheit_origin - 32 ) * ( 5 / 9 )
degree_fahrenheit = degree_celsius_origin * ( 9 / 5 ) + 32

print(degree_fahrenheit_origin, 'degree in Fahrenheit is', degree_celsius, 'degree in Celsius')
print(degree_celsius_origin,'degree in Celsius is', degree_fahrenheit, 'degree in Fahrenheit ')

##### split
print('')
print('############################################################################')
