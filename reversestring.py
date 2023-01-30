# Write a Python program to reverse a string.
# ﻿Sample String : "1234abcd"
# Expected Output : "dcba4321"
def rev(x):    
    x= x[::-1]
    return x
x=input("enter string : ")
print("o_g: ", x)
print("reversed is : ",rev(x))