# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
# ﻿Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def cal(s):
    d={"u_c":0,"l_c":0}
    for c in s:
        if c.isupper():
            d["u_c"]+=1
        elif c.islower():
            d["l_c"]+=1
        else:
            pass
    print("o_g: " , s)
    print("No. of Upper case characters : ",d["u_c"])
    print("No. of Lower case Characters :", d["l_c"])

cal("Hai Frens")
