# Read inputs for set: s
_ = input()
s = set(map(int, input().split()))

# Loop through all the different operations
for _ in range(int(input())):
    
    # Split to methods and args, args being optional
    method, *args = input().split()
    
    # Splat (*) operator unpacks the elements in the tuple   
    getattr(s, method)(*map(int, args)) 

# Print sum of elements in 's'
print(sum(s))