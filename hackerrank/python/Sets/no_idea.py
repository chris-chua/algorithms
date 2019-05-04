# n and m not required
_ = input()

# Initializing array: arr and two sets: A, B
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# Check if elements in array are in sets A or B and print output
happiness = sum([(i in A) - (i in B) for i in arr])
print(happiness)