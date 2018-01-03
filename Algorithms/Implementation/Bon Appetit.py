#!/bin/python

import sys
def months_and_days_in_Year(Year):
    arr ={}
    for i in range(1,13):
        if i < 8 and i != 2:
            if i%2 == 0:
                arr[i] = range(1,31)
            else:
                arr[i] = range(1,32)
        if i == 2:
            if Year == 1918:
                if Year%4 == 0:
                    arr[i] = range(14,30)
                else:
                    arr[i] = range(14,29)
            if Year < 1918:
                if Year%4 == 0:
                    arr[i] = range(1,30)
                else:
                    arr[i] = range(1,29)
            if Year > 1918:
                if (Year%400 == 0) or (Year%4 == 0 and Year%100 != 0):
                    arr[i] = range(1,30)
                else:
                    arr[i] = range(1,29)
        if i >= 8:
            if i%2 == 0:
                arr[i] = range(1,32)
            else:
                arr[i] = range(1,31)
    return arr
    
def solve(year):
    # Complete this function
    count = 0
    My_day = 0
    My_month = 0
    arr = months_and_days_in_Year(year)
    for month,days in arr.items():
        for day in days:
            if count < 256:
                My_day = day
                My_month = month
                count = count + 1
    if My_day < 10:
        My_day = '0'+str(My_day)
        if My_month < 10:
            out_put = My_day+'.'+ '0'+str(My_month)+'.'+ str(year)
        else:
            out_put = My_day+'.'+ str(My_month)+'.'+ str(year)
    else:
        if My_month < 10:
            out_put = str(My_day)+'.'+ '0'+str(My_month)+'.'+ str(year)
        else:
            out_put = str(My_day)+'.'+ str(My_month)+'.'+ str(year)
    return out_put
    
year = int(raw_input().strip())
result = solve(year)
print(result)
