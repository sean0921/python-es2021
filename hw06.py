#!/usr/bin/env python3

'''
Fibonacci:
n   result
0   0
1   1
2   2
3   3=1+2
4   5=2+3
5   8=3+5
6   13=5+8
7   21=8+13
8   34=13+21
'''

import sys

### HW1 (functions)

def printerr(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def fibonacci(serial_number: str) -> int:
    try:
        serial_number = int(serial_number)
        int(serial_number)
    except ValueError:
        printerr('\x1b[1;31mPlease input a natural number!\x1b[0m')
        sys.exit(1)
    if serial_number < 0:
        printerr('\x1b[1;31mPlease input a natural number!\x1b[0m')
        sys.exit(1)
    if serial_number == 0:
        return 0
    if serial_number == 1:
        return 1
    fib_result = fibonacci( serial_number - 1 ) + fibonacci( serial_number - 2 )
    return fib_result

### HW1

this_input = input('Please input a natural number:')
this_output = fibonacci( this_input )

print(this_output)

### HW2

stored_values = []

print('Please input a real number: (Ctrl+C or Ctrl+D to stop the input)')
while True:
    try:
        a = input()
        if a=='EOF' or a=='':
            break
        a = float(a)
    except ValueError:
        printerr('\x1b[1;31mPlease input a REAL number!\x1b[0m')
        continue
    except KeyboardInterrupt:
        break
    except EOFError:
        break
    stored_values.append(a)  #stored_values += [a]
    del(a)
    continue

if len(stored_values) == 0:
    printerr('\x1b[1;33mEmpty List!\x1b[0m')
else:
    print('list content:', stored_values)
    print('Numbers of list:', len(stored_values))
    print('Summary of list:', sum(stored_values))
    print('Maximum:', max(stored_values))
    print('Minimun:', min(stored_values))
    print('Average:', sum(stored_values)/len(stored_values))
