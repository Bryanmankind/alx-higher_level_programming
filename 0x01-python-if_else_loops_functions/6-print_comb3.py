#!/usr/bin/python3
# 6-print_comb3.py

for number in range(10):
    for number1 in range(number + 1, 10):
        print("{}{}".format(number,number1),end = ", ")
