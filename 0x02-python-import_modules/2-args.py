#!/usr/bin/python3
if __name__ != "__main__":
    exit
import sys
count = len(sys.argv) - 1
if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))

for i in range(0, count):
    print("{}: {}".format(i +1, sys.argv[i+1]))
