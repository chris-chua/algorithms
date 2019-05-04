def print_rangoli(n):
    import string
    alpha = string.ascii_lowercase
   
    L = []
    for i in range(n):
        # Getting the right half of each line
        s = '-'.join(alpha[i:n])
        # Joining the left half to the right half of each line
        # and fill the rest of the spaces with '-'
        L.append((s[::-1] + s[1:]).center(4*n-3, '-'))
   
    # Joining the top half of pattern with bottom half
    print('\n'.join(L[::-1] + L[1:]))