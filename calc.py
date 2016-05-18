#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import sys

def main():
    """Join command-line arguments and pass them to unitcalc(), then print."""
    calculation = ''.join(sys.argv[1:])
    print (calc(calculation))

def calc(s):
    """Parse a string describing an operation on quantities with units."""

    index = 0
    for char in s:
        if(not char.isdigit()):
            break
        index = index + 1
    
    num1 = (s[0:index])
    num2 = (s[index:len(s)])
    operation = s[index]

    if operation=='+':
        return int(num1)+int(num2)
    elif operation=='-':
        return int(num1)-int(num2)
    elif operation=='*':
        return int(num1)*int(num2)
    elif operation=='/':
        return int(num1)/int(num2)


if __name__ == "__main__": main()
