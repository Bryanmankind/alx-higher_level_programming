#!/usr/bin/python3
#3-print_alphabt.py

for letter in range(97, 123):
    if letter not in (113, 101):
        print("{}".format(chr(letter)), end="")
