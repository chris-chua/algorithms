# Read inputs
_ = input()
English = set(input().split())
_ = input()
French = set(input().split())

# Print length of intersection of sets       
print(len(English.intersection(French)))