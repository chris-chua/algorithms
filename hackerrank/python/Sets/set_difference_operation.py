# Read inputs
_ = input()
English = set(input().split())
_ = input()
French = set(input().split())

# Print length of difference of sets       
print(len(English.difference(French)))