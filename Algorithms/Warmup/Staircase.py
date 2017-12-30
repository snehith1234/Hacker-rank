def staircase(n):
    count = 1
    # Complete this function
    for i in range(n-1,-1,-1):
        print " "*i + '#'*count
        count = count + 1
if __name__ == "__main__":
    n = int(raw_input().strip())
    staircase(n)
