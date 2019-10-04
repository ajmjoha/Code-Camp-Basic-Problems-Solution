# -*- coding: utf-8 -*-
# -*- coding in this time : utf-8 -*-
"""
Created on Sat Oct 05 04:06:27 2019

@author: Ajm joha
"""
a,b,c,d,e = [int(k) for k in input("Enter marks of five subjects: ").split()]

total = a + b + c + d + e
average = total / 5
percentage = (total / 500) * 100

print ("\nTotal = %.f" % total)
print (" \nAverage = %.f" % average)
print ("  \nPercentage = %.2f" % percentage)
