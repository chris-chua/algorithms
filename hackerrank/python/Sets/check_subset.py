# Loop and read inputs into sets 'A' and 'B'
for _ in range(int(input())):
    _, A = input(), set(input().split())
    _, B = input(), set(input().split())

# Print result of A being a subset of B
print(A <= B)