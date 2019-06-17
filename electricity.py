# -*- coding: utf-8 -*-
m=int(input("Enter the meter reading:"))
if(m<100):
    bill=2*m
elif(100<m<200):
    bill=3*m
elif(200<m<300):
    bill=5*m
else:
    bill=6*m
    
print(bill)
    
