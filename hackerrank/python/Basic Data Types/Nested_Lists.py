# Creating a list of name, grades in list: classgrades
n = int(input())
classgrades = [[input(), float(input())] for _ in range(n)]

# Sort an unique list of grades in ascending order, and get the second one
second_highest = sorted(list(set([grades for name, grades in classgrades])))[1]

# Output the names on a new line, sorted in alphabetical order
print('\n'.join([name for name, grades in sorted(classgrades) if grades==second_highest]))