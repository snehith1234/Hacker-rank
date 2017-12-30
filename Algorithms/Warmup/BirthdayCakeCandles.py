def birthdayCakeCandles(n, ar):
    # Complete this function
    count = 0
    maxi = max(ar)
    for i in range(len(ar)):
        if ar[i] == maxi:
            count = count + 1
    return count
n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
