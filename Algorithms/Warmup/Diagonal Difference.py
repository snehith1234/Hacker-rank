
def input_set(Matrix_Size):
    arr1 =[]
    for i in range(Matrix_Size):
        arr=[]
        arr[0:Matrix_Size] = raw_input().split()
        arr1.append(arr)
    return arr1
def diagonal_differenc(arr1):
    a = 0
    c = len(arr1)-1
    Sum1 = 0
    Sum2 = 0
    while a < len(arr1):
        Sum1 = Sum1 + int(arr1[a][a])
        Sum2 = Sum2 + int(arr1[a][c])
        a = a + 1
        c = c - 1
    Sum = Sum1 - Sum2
    if Sum < 0:
        Sum = -1 * Sum
        print Sum
    else:
        print Sum
def main():
    Matrix_Size = raw_input()
    Matrix_Size  = int(Matrix_Size)
    input_arr = input_set(Matrix_Size)
    diagonal_differenc(input_arr)

if __name__=="__main__":
    main()
