n, m = map(int, input().split())

# Create the pattern above the Welcome line. Repeat the '.|.' pattern for 2i+1 times.
# Place pattern in the center and fill the rest of the space with '-'.
pattern = [('.|.' * (2*i+1)).center(m, '-') for i in range(n//2)]

# Join the top pattern, Welcome line, and bottom pattern(the reversed of top pattern).
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])) 