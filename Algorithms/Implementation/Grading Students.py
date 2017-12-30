def solve(grades):
    # Complete this function
    arr=[]
    for i in range(len(grades)):
        value = grades[i]%5
        if value != 0:
            value1 = grades[i]/5
            grade = (value1 + 1)*5
            grade_diff = grade - grades[i]
            if grade_diff < 3 and grade >= 40:
                arr.append(grade)
            else:
                arr.append(grades[i])
        else:
            arr.append(grades[i])        
    return arr

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))

