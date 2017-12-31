def getTotalX(a, b):
    # Complete this function
    a = sorted(a)
    b = sorted(b)
    count = 0
    num = a[-1]
    while num <= b[0]:
        arr =[]
        for i in range(len(a)):
            if num % a[i]  == 0:
                arr.append(num)
        while len(arr) == len(a):
            brr = []
            for j in range(len(b)):
                if b[j] % num == 0:
                    brr.append(num)
            while len(brr) == len(b):
                count = count + 1
                brr =[]
            arr=[]
        num = num + 1
    return count
            
           
        
            

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    total = getTotalX(a, b)
    print total
