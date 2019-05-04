# initializing empty dict: student_marks
student_marks = {}

# read inputs and update dict    
for _ in range(int(input())):
        name, *score = input().split()
        scores = list(map(float, score))
        student_marks[name] = scores

# read input: query_name    
query_name = input()

# calculate mean marks of student
mean_marks = sum(student_marks[query_name])/len(student_marks[query_name])

# print result
print('{0:.2f}'.format(mean_marks))