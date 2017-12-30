def plusMinus(arr):
    # Complete this function
    pos = 0
    neg = 0
    zeros = 0
    i = 0
    while i < len(arr):
        if arr[i] < 0:
            neg = neg + 1
        if arr[i] == 0:
            zeros = zeros + 1
        if arr[i] > 0:
            pos = pos + 1
        i = i + 1
    return pos,neg,zeros,len(arr)
            
if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    pos,neg,zeros,length = plusMinus(arr)
    X = float(pos)/float(length)
    Y = float(neg)/float(length)
    Z = float(zeros)/float(length)
    print "%.6f"%(X)
    print "%.6f"%(Y)
    print "%.6f"%(Z)
