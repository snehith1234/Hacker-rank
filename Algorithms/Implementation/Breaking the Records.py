def breakingRecords(score):
    # Complete this function
    key_min = score[0]
    key_max = score[0]
    result=[]
    count_max = 0
    count_min = 0
    for i in range(1,len(score)):
        if score[i] > key_max:
            key_max = score[i]
            count_max = count_max + 1
        if score[i] < key_min:
            key_min = score[i]
            count_min = count_min + 1
    result.append(count_max)
    result.append(count_min)
    return result
          
        
if __name__ == "__main__":
    n = int(raw_input().strip())
    score = map(int, raw_input().strip().split(' '))
    result = breakingRecords(score)
    print " ".join(map(str, result))

