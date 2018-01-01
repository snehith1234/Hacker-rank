#!/bin/python


def bonAppetit(n, k, b, ar):
    # Complete this function
    b_extra = 0
    total = 0
    for i in xrange(len(ar)):
        if i == k:
            b_extra = ar[i]
        else:
            total = total + ar[i]
    if total/2 == b:
        return "Bon Appetit"
    else:
        return b_extra/2
     
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
