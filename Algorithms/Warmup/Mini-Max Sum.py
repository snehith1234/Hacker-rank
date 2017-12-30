def miniMaxSum(arr):
    # Complete this function
    arr1 = sorted(arr)
    maxi = 0
    mini = 0
    for i in range(len(arr1)):
        if i != 0:
            maxi = maxi + arr1[i]
        if i != len(arr1)-1:
            mini = mini + arr1[i]
    print mini,maxi
if __name__ == "__main__":
    arr = map(int, raw_input().strip().split(' '))
    miniMaxSum(arr)
