#!/usr/bin/python3
# 5-print_comb2.py

for number in range(100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
