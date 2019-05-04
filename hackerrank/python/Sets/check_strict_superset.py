# Read input into set 'A'
A = set(input().split())

# Print True if and only if A > all sets 
print(all(A > set(input().split()) for _ in range(int(input()))))