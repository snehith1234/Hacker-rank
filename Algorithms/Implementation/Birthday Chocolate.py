def solve(n, s, d, m):
    # Complete this function
    count = 0
    for i in range(len(s)-(m-1)):
        num = m
        sum = 0
        j = i
        while num != 0:
            sum = sum + s[j]
            j = j + 1
            num = num - 1
        if sum == d:
            count = count + 1
    return count 
            
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
