def kangaroo(x1, v1, x2, v2):
    # Complete this function
    if x2> x1 and v2 > v1:
        out_put ='NO'
        return out_put
    if v2 == v1:
        out_put ='NO'
        return out_put
    elif((x2-x1)%(v1-v2)) == 0:
        out_put ='YES'
        return out_put
    else:
        return 'NO'

        
x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

