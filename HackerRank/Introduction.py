# Python If-Else
'''
Task
Given an integer, n, perform the following conditional actions:
If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
'''
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0:
        if n > 1 and n < 6:
            print('Not Weird')
        elif n > 5 and n < 21:
            print('Weird')
        elif n > 20:
            print('Not Weird')

# Arithmetic Operators
'''
Task
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)

# Python Division
'''
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.
No rounding or formatting is necessary.
'''
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

# Loops
'''

'''