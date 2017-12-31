def divisibleSumPairs(n, k, ar):
    # Complete this function
    count = 0
    i = 0
    while i < len(ar)-1:
        for j in range(len(ar)):
            if i != j:
                if i < j and ((ar[i]+ar[j])%k)== 0:
                    count = count + 1
        i = i + 1
    return count
n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
result = divisibleSumPairs(n, k, ar)
print(result)
