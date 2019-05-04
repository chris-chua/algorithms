# Read elements into set 'A'
_ = int(input())
A = set(map(int, input().split()))

# Loop and read inputs
for _ in range(int(input())):
    method = input().split(' ')[0]
    B = set(map(int, input().split()))
    getattr(A, method)(B)

# Print the sum of elements in set A   
print(sum(A))