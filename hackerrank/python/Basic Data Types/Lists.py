# initializing empty list: lst
lst = []

# read input from each line
for _ in range(int(input())):
    # split line into method and optional args
    method, *args = input().split()
    # perform each method and supply parameters with splat operator
    print(lst) if method == 'print' else getattr(lst, method)(*(map(int, args)))