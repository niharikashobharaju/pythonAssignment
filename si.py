# -*- coding: utf-8 -*-
p=int(input("Enter the Principle:"))
t=int(input("Enter the Time:"))
r=int(input("Enter the rate of Interest:"))
def si(p,t,r):
    i=(p*t*r)/100
    return i
    
res=si(p,t,r)
print("Simple Interest:",res)
