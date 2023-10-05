#!/usr/bin/python3
if __name__ != "__main__":
    exit
import sys
from calculator_1 import add, sub, mul, div

count = len(sys.argv) - 1
if count != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)


sum = 0

for i in range(0, count):
    sum += int(sys.argv[i+1])






print("{} + {} = {}".format(a, b, add(a, b)))
print("{} - {} = {}".format(a, b, sub(a, b)))
print("{} * {} = {}".format(a, b, mul(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
