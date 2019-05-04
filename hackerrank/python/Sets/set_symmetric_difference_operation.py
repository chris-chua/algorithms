# Read inputs
_ = input()
English = set(input().split())
_ = input()
French = set(input().split())

# Get the unique elements that appear in either sets but not both
unique = English.symmetric_difference(French)

# Print length of 'unique'       
print(len(unique))