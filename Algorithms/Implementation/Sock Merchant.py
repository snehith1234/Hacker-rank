
N = int(raw_input("Enter the weights::"))
arr = {}
for i in xrange(N):
    wL= raw_input()
    wR = raw_input()
    if wR =='':
        arr[i] = [wL,'0']
    if wL =='':
        arr[i] = ['0',wR]
    else:
        arr[i] = [wL,wR]

