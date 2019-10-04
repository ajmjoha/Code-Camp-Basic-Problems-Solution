# -*- coding: utf-8 -*-
# -*- coding in this time : utf-8 -*-
"""
Created on Sat Oct 05 03:36:04 2019

@author: Ajm joha
"""
days =int(input("Enter days: "))
years = days/365
#weeks = (days -(years * 365)) /7
weeks = int((days % 365) /7)
#day = days - ((years * 365) + (weeks * 7))
day = (days % 365) % 7

print(days,"days = %.f "%years,"year/s, ",weeks,"week/s ""and",day,"day/s ")


