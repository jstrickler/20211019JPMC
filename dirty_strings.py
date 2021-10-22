#!/usr/bin/python3

spam = [ 
    "Spam", 
    "eggs  ",
    "   spam    ",
    "     spam spam     ", 
    "SPAM	", 
    "       SPAM and eggs    ",
    "Spam",
    "   Spam,    spam, spam,    spam, spam, eggs, and spam      ",
]

def cleanup(s):
    pass

for dirty in spam:
    clean = cleanup(dirty)
    print(f">{dirty}< >{clean}<")
