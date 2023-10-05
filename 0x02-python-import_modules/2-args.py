#!/usr/bin/python3
if __name__ != "__main__":
    exit
import sys
count = len(sys.argv) - 1
if count == 0:
    print(f"{count} arguments.")
elif count == 1:
    print("1 argument:")
else:
    print(f"{count} arguments:")

for i in range(0,count):
    print(f"{i +1}: {sys.argv[i+1]} ")
