
def migratoryBirds(n, ar):
    # Complete this function
    most_commen = 0
    arr={}
    for i in range(1,6):
        count = 0
        if i in ar:
            for j in range(len(ar)):
                if i == ar[j]:
                    count = count + 1
        arr[i] = count
    print arr
    key = len(arr) + 1
    for i,j in enumerate(arr.values()):
        if j == max(arr.values()):
            if i < key:
                key =i
    return key+1
    

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
