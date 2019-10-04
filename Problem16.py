# -*- coding: utf-8 -*-
# -*- coding in this time : utf-8 -*-
"""
Created on Sat Oct 05 04:54:05 2019

@author: Ajm joha
"""
principle = int(input("Enter principle(amount): "))
time = int(input("Enter time: "))
rate = float(input("Enter rate: "))
#SI = (principle * time * rate) / 100
CI = principle * pow((1 + rate / 100), time)
#print ("Simple Interest = ",SI)
print("Compound Interest = ",CI)
