# Read inputs
_ = input()
English = set(input().split())
_ = input()
French = set(input().split())

# Print length of union of sets       
print(len(English.union(French)))