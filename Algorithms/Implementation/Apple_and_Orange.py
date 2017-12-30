def appleAndOrange(s, t, a, b, apple, orange):
    # Complete this function
    arr =[]
    apple_count = 0
    orange_count = 0
    for i in range(len(apple)):
        fall_apple = a + apple[i]
        if fall_apple >= s and fall_apple <= t :
            apple_count = apple_count + 1
    for i in range(len(orange)):
        fall_orange = b + orange[i]
        if fall_orange >= s and fall_orange <= t :
            orange_count = orange_count + 1  
    arr.append(apple_count)
    arr.append(orange_count)
    return arr
if __name__ == "__main__":
    s, t = raw_input().strip().split(' ')
    s, t = [int(s), int(t)]
    a, b = raw_input().strip().split(' ')
    a, b = [int(a), int(b)]
    m, n = raw_input().strip().split(' ')
    m, n = [int(m), int(n)]
    apple = map(int, raw_input().strip().split(' '))
    orange = map(int, raw_input().strip().split(' '))
    result = appleAndOrange(s, t, a, b, apple, orange)
    print "\n".join(map(str, result))


