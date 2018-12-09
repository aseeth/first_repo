# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n = int(input("enter any num:"))
m = n 
rev = 0
while n>0:
    dig = n%10
    rev = rev *10+dig
    n = n//10
if m == rev:
    print("this is the palindrom")
else:
    print("not a palindrom")

