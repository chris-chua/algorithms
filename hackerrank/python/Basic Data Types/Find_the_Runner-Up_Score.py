# read input
n = int(input())
arr = map(int, input().split())

# remove duplicates in array: arr
unique_arr = list(set(arr))

# print the last second element in sorted array
print(sorted(unique_arr)[-2])