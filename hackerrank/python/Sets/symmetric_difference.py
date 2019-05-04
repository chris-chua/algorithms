# Read inputs
_ = input()
set_M = set(map(int, input().split()))
_ = input()
set_N = set(map(int, input().split()))

# Get the unique elements that appear in either sets but not both
unique = set_M.symmetric_difference(set_N)

# Print the elements of the sorted unique set on each line
print(*sorted(unique), sep='\n')