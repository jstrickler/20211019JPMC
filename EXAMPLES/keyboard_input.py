#!/usr/bin/env python

name = input("What is your name: ")
quest = input("What is your quest? ")
print(name, "seeks", quest)

raw_num = input("Enter number: ")  # <1>
num = float(raw_num)  # <2>

print("2 times", num, "is ", 2 * num)

print("25\u00B0")